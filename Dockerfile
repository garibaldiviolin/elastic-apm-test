FROM python:3.8.6-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY Pipfile Pipfile.lock /code/
RUN apt-get update && \
    apt-get install gcc libpq-dev python-dev -y && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system && \
    apt-get clean
ADD . /code/

EXPOSE 8000
