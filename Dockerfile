FROM python:latest

ENV APP_HOME=/app

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME

RUN apt-get update && apt-get install build-essential bash cmake pkg-config -y

#RUN pip install -r requirements.txt

COPY . $APP_HOME/