FROM python:latest

ENV APP_HOME=/app

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME

RUN apt-get update && apt-get install build-essential bash cmake pkg-config -y

# Install chrome driver
COPY ./scripts $APP_HOME/scripts
RUN $APP_HOME/scripts/install_chromedriver.sh

# Install python libraries
COPY requirements.txt $APP_HOME/
RUN pip install -r requirements.txt
