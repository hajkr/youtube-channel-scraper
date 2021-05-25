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
pip install hajkr_youtube_scraper
```

### Usage

```python
from hajkr_youtube_scraper.crawler import Crawler

crawler = Crawler(channel_url)
crawled_videos = crawler.crawl()
```

## Use as a script

### Installation

```bash
git clone https://github.com/hajkr/youtube-scraper.git
cd youtube_scraper

make run
```

### Usage

You should run it in a docker container otherwise you need to set up chrome driver in your environment.

```bash
make run
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
