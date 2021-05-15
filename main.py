from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from video import Video
from crawler import Crawler


channel_url = "https://www.youtube.com/user/anzecokl/videos"

crawler = Crawler("https://www.youtube.com/user/anzecokl")
crawler.crawl()
