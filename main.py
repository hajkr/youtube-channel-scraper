import csv
import locale
from crawler import Crawler


def write_to_csv(items, filename):
    keys = items[0].keys()
    with open(filename, 'w', encoding=locale.getpreferredencoding()) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(items)


channel_url = "https://www.youtube.com/user/anzecokl/videos"

crawler = Crawler("https://www.youtube.com/user/anzecokl")
crawled_videos = crawler.crawl()

print("Writing to csv...")
write_to_csv(crawled_videos, "videos.csv")
