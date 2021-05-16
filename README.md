# Youtube scraper

A Python script that scrapes videos from a Youtube channel and stores them in a CSV document.

Video attributes to be scraped:
* `url`
* `title`
* `description`
* `author`
* `published_at`
* `thumbnail`

## Installation guide

```bash
git clone https://github.com/hajkr/youtube-scraper.git
cd youtube-scraper

make run
```

## Usage guide

```bash
make to_container

python youtube-scraper "yt_channel_url" --filename "output/videos.csv"
```

### Available arguments
```bash
positional arguments:
  channel_url                   Youtube channel URL

optional arguments:
  -h, --help                    show this help message and exit
  --filename FILENAME           Output file
  --stop_video_id STOP_VIDEO_ID Youtube video ID that indicates to stop crawling
```
