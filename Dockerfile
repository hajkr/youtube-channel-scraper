FROM python:latest

ENV APP_HOME=/app

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get install build-essential bash cmake pkg-config -y

RUN apt-get install libnss3 google-chrome-stable -y

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 90.0.4430.24
ENV CHROMEDRIVER_DIR /chromedriver

# Download and install Chromedriver
RUN mkdir $CHROMEDRIVER_DIR
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

COPY requirements.txt $APP_HOME/
RUN pip install -r requirements.txt
