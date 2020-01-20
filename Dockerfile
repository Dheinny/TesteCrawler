FROM python:3.6-alpine3.9

RUN apk update \
    && apk add --virtual build-deps gcc curl g++ libffi-dev openssl-dev \
    && apk add libxml2-dev libxslt-dev python3-dev musl-dev \
    && apk add bash

RUN pip3 install sqlalchemy pymysql
RUN pip3 install scrapy

RUN mkdir /app-crawler
ADD . /app-crawler
WORKDIR /app-crawler