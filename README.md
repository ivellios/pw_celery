# Playing with Celery

This is a simple example of using celery with RabbitMQ.

## Requirements

* docker (with docker-compose)
* python 2.7/3.5+
* optionally virtualenv

## How to install

* Run `docker-compose up` to setup RabbitMQ container
* Setup your virtualenv
* Install requirements with `pip install -r requirements.txt`

And now you can play with prepared tasks or add new one.

## Basice use

By default there's a simple `use.py` file with example that will download website HTML from given URL.

* Run with `python use.py PAGE_URL` applying your own page download URL.
