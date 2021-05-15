from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def build_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome('chromedriver', chrome_options=chrome_options)


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


VIDEOS_SELECTOR = 'ytd-grid-renderer.ytd-item-section-renderer #items > ytd-grid-video-renderer'

class Crawler:
    def __init__(self, channel_url):
        self.channel_url = channel_url
        self.browser = build_browser()

    def crawl(self):
        print(self.channel_url)

        self.navigate_to_videos()
        self.load_all_pages()
        video_urls = self.extract_video_urls()
        pprint(video_urls)
        print(len(video_urls))

        self.browser.close()

    def extract_video_urls(self):
        return list(map(
            lambda element: element.find_element_by_css_selector('ytd-thumbnail a').get_attribute('href'),
            self.find_video_elements()
        ))

    def count_video_elements(self):
        return len(self.find_video_elements())

    def find_video_elements(self):
        return self.browser.find_elements_by_css_selector(VIDEOS_SELECTOR)

    def navigate_to_videos(self):
        videos_url = f'{self.channel_url}/videos'
        self.browser.get(videos_url)
        self.browser.find_element_by_css_selector('button').click()

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
