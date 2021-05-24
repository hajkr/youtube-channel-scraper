import argparse
from crawler import Crawler
from utils import write_to_csv
from selenium.common.exceptions import TimeoutException

parser = argparse.ArgumentParser()
parser.add_argument('channel_url', type=str, help="Youtube channel URL")
parser.add_argument('--filename', type=str, help="Output file", default='output/videos.csv')
parser.add_argument('--stop_video_id', type=str, help="Youtube video ID that indicates to stop crawling", default=None)
parser.add_argument('--max_videos', type=int, help="Max videos to crawl", default=1000)
parser.add_argument('--proxy', type=str, help="Proxy IP", default=None)
parser.add_argument('--screenshot_filename', type=str, help="Path to exceptions screenshot", default='output/screenshot.png')

args = parser.parse_args()

print(args)

crawler = Crawler(args.channel_url, stop_id=args.stop_video_id, max_videos=args.max_videos, proxy_ip=args.proxy)
try:
    crawled_videos = crawler.crawl()
    write_to_csv(crawled_videos, args.filename)
    print(f"{len(crawled_videos)} videos saved to {args.filename}")
except TimeoutException as e:
    print("An exception occurred: ", e)
    crawler.browser.get_screenshot_as_file(args.screenshot_filename)

