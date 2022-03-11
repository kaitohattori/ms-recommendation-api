FROM python:3.7-slim-buster

RUN apt-get update && apt-get -y install gcc libpq-dev g++

RUN cd
RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python main.py
