app_name = youtube_scraper

run:
	echo -ne "\033]0;$(app_name)\007" && docker compose up

build_and_run:
	echo -ne "\033]0;$(app_name)\007" && docker compose up --build

to_container:
	echo -ne "\033]0;$(app_name)\007" && docker exec -it $(app_name) bash

requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt