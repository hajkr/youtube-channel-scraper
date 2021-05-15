import argparse
from crawler import Crawler
from utils import write_to_csv

parser = argparse.ArgumentParser()
parser.add_argument('channel_url', type=str, help="Youtube channel URL")
parser.add_argument('--filename', type=str, help="Output file", default='output/videos.csv')
parser.add_argument('--stop_video_id', type=str, help="Youtube video ID that indicates to stop crawling", default=None)
args = parser.parse_args()

print(args)

crawler = Crawler(args.channel_url, stop_id=args.stop_video_id)
crawled_videos = crawler.crawl()

if len(crawled_videos):
    write_to_csv(crawled_videos, args.filename)
    print(f"Saved to: {args.filename}")
else:
    print("No videos found.")
