# YouTube scraper

A Python script that scrapes videos from a Youtube channel.

It takes a YouTube channel URL as an input and produces a list of videos as an output.

Video attributes:
* `url`
* `title`
* `description`
* `author`
* `published_at`
* `thumbnail`

## Use as a library

### Requirements

* Install chromedriver at `/chromedriver`. For more details refer to [scripts/install_chromedriver.sh](scripts/install_chromedriver.sh)

### Installation

```bash
pip3 install hajkr_youtube_scraper
```

### Usage

```python
from hajkr_youtube_scraper.crawler import Crawler

crawler = Crawler(channel_url, stop_id=stop_video_id, max_videos=max_videos, proxy_ip=proxy)
try:
    crawled_videos = crawler.crawl()
except TimeoutException as e:
    # Works well for debugging
    print("An exception occurred: ", e)
    crawler.browser.get_screenshot_as_file(screenshot_path)
```

## Use as a script

### Installation

```bash
git clone https://github.com/hajkr/youtube-scraper.git
cd youtube_scraper

make run
```

### Usage

```bash
make to_container

python hajkr_youtube_scraper "https://www.youtube.com/channel/CHANNEL_ID"
```

### Available arguments

```bash
positional arguments:
  channel_url           Youtube channel URL

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME   Output file
  --stop_video_id STOP_VIDEO_ID
                        Youtube video ID that indicates to stop crawling
  --max_videos MAX_VIDEOS
                        Max videos to crawl
  --proxy PROXY         Proxy IP
  --screenshot_filename SCREENSHOT_FILENAME
                        Path to exceptions screenshot
```
