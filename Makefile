SHELL:=/bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
BASE_PATH=${PWD}
PYTHON_EXEC=python

include .env

init: down _build up

up:
	docker-compose up -d  --remove-orphans
stop:
	docker-compose stop
_build:
	sudo docker-compose build

build: stop _build up

down:
	docker-compose down

install:
	docker-compose exec web poetry install

chown:
	sudo chown -R "${USER}:${USER}" ./

startapp:
	docker-compose exec web python manage.py startapp ${ARGS}
	sudo chown -R "${USER}:${USER}" ./

log:
	docker-compose logs -f web 

restart_web:
	docker-compose restart web

makemigrations:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate

migrate:
	docker-compose exec web python manage.py migrate

sh:
	docker-compose exec ${ARGS} bash

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

load_products:
	docker-compose exec web python manage.py load_products

flake8:
	docker-compose exec web isort .

test:
	docker-compose exec web py.test "${ARGS}"