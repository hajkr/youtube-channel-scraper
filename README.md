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

python main.py "yt_channel_url" --filename "output/videos.csv"
```
