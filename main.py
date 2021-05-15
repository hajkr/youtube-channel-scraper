import csv
import locale
import argparse
from crawler import Crawler


def write_to_csv(items, filename):
    keys = items[0].keys()
    with open(filename, 'w', encoding=locale.getpreferredencoding()) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(items)


parser = argparse.ArgumentParser()
parser.add_argument('channel_url', type=str, help="Youtube channel URL")
parser.add_argument('--filename', type=str, help="Output file", default='output/videos.csv')
args = parser.parse_args()

print(args)

crawler = Crawler(args.channel_url)
crawled_videos = crawler.crawl()

print("Writing to csv...")
write_to_csv(crawled_videos, args.filename)
