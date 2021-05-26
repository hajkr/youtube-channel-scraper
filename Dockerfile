FROM python:3.9.5

ENV APP_HOME=/app
ENV HOME=/root
ENV PATH=$PATH:/root/.poetry/bin

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME

RUN apt-get update && apt-get install build-essential bash cmake pkg-config -y

# Install chrome driver
COPY ./scripts $APP_HOME/scripts
RUN $APP_HOME/scripts/install_chromedriver.sh

# Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Install python libraries
COPY pyproject.toml $APP_HOME/
COPY poetry.lock $APP_HOME/
RUN poetry install
