import setuptools

setuptools.setup(
    name="hajkr_youtube_scraper",
    version="0.0.41",
    author="Tadej Hribar",
    author_email="tadej.996@gmail.com",
    description="A package for scraping youtube",
    url="https://github.com/hajkr/youtube-scraper",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
    ],
)
