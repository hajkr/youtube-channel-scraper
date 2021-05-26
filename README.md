# YouTube Channel Scraper

Scrapes videos from a YouTube channel using Python.

It takes a YouTube channel URL as an input and produces a list of videos as an output.

Video attributes:
* `url`
* `title`
* `description`
* `author`
* `published_at`
* `thumbnail`

## Requirements

* Install chromedriver at `/chromedriver`. For more details refer to [scripts/install_chromedriver.sh](scripts/install_chromedriver.sh)

## Install

```bash
pip install youtube-channel-scraper
```

## Usage

```python
from youtube_channel_scraper.scraper import YoutubeScraper

scraper = YoutubeScraper(channel_url)
crawled_videos = scraper.scrape()
```

### Optional parameters

* *stop_id:* stop scraping when this video ID is encountered. Older videos are always scraped first.
* *max_videos:* maximum amount of videos to scrape
* *proxy_ip:* proxy IP with port 


## CLI usage

### Install and run in Docker

Using docker there is no need to manually install chrome driver in your environment.

```bash
git clone https://github.com/hajkr/youtube-channel-scraper.git
cd youtube_channel_scraper

make run
```

### Usage

You should run it in a docker container otherwise you need to set up chrome driver in your environment.

```bash
make run
make to_container

python youtube_channel_scraper "https://www.youtube.com/channel/CHANNEL_ID"
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
