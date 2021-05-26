app_name = youtube_scraper

run:
	echo -ne "\033]0;$(app_name)\007" && docker compose up

build_and_run:
	echo -ne "\033]0;$(app_name)\007" && docker compose up --build

to_container:
	echo -ne "\033]0;$(app_name)\007" && docker exec -it $(app_name) bash

init:
	touch requirements.txt
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

compile:
	rm -rf build/ dist/ youtube_channel_scraper.egg-info/
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*