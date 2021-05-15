import time
from pprint import pprint
import urllib.parse as urlparse
from urllib.parse import parse_qs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ElementsLengthChanges(object):
    def __init__(self, selector):
        self.selector = selector
        self.initial_length = None
        self.driver = None

    def __call__(self, driver):
        self.driver = driver
        self.set_initial_length()
        return self.count_elements() > self.initial_length

    def set_initial_length(self):
        if self.initial_length is None:
            self.initial_length = self.count_elements()

    def count_elements(self):
        return self.driver.find_elements_by_css_selector(self.selector)


def build_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome('chromedriver', chrome_options=chrome_options)


def url_to_thumbnail(url):
    parsed = urlparse.urlparse(url)
    video_id = parse_qs(parsed.query)['v'][0]
    return f"https://i3.ytimg.com/vi/{video_id}/hqdefault.jpg"


VIDEOS_SELECTOR = 'ytd-grid-renderer.ytd-item-section-renderer #items > ytd-grid-video-renderer'
VIDEO_TITLE_SELECTOR = 'ytd-video-primary-info-renderer h1'
VIDEO_DESCRIPTION_SELECTOR = 'ytd-video-secondary-info-renderer #description'
VIDEO_AUTHOR_SELECTOR = 'ytd-video-secondary-info-renderer ytd-channel-name a'
VIDEO_PUBLISHED_AT_SELECTOR = 'ytd-video-primary-info-renderer #date yt-formatted-string'


class Crawler:
    def __init__(self, channel_url):
        self.channel_url = channel_url
        self.browser = build_browser()

    def __del__(self):
        self.browser.close()

    def crawl(self):
        print(self.channel_url)

        self.navigate_to_videos()
        self.load_all_pages()

        print("Extracting video urls...")
        video_urls = self.extract_video_urls()

        crawled_videos = []
        for url in video_urls:
            print(url)

            self.navigate_to_video(url)
            crawled_videos.append(self.extract_video_attributes(url))

        return crawled_videos

    def extract_video_urls(self):
        return list(map(
            lambda element: element.find_element_by_css_selector('ytd-thumbnail a').get_attribute('href'),
            self.find_video_elements()
        ))

    def extract_video_attributes(self, url):
        return {
            "url": url,
            "title": self.browser.find_element_by_css_selector(VIDEO_TITLE_SELECTOR).text,
            "description": self.browser.find_element_by_css_selector(VIDEO_DESCRIPTION_SELECTOR).text,
            "author": self.browser.find_element_by_css_selector(VIDEO_AUTHOR_SELECTOR).text,
            "published_at": self.browser.find_element_by_css_selector(VIDEO_PUBLISHED_AT_SELECTOR).text,
            "thumbnail": url_to_thumbnail(url),
        }

    def count_video_elements(self):
        return len(self.find_video_elements())

    def find_video_elements(self):
        return self.browser.find_elements_by_css_selector(VIDEOS_SELECTOR)

    def navigate_to_videos(self):
        videos_url = f'{self.channel_url}/videos'
        self.browser.get(videos_url)
        self.browser.find_element_by_css_selector('button').click()

    def navigate_to_video(self, url):
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, VIDEO_TITLE_SELECTOR))
        )

    def load_all_pages(self):
        while True:
            try:
                self.load_next_page()
                print(self.count_video_elements())
            except TimeoutException:
                break

    def load_next_page(self):
        self.browser.execute_script("window.scrollTo(0, Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight))")
        WebDriverWait(self.browser, 5).until(ElementsLengthChanges(VIDEOS_SELECTOR))
