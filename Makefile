DOCKER_COMPOSE = docker-compose
SERVICE_NAME = web

# Команды для управления Docker
.PHONY: build up down run shell createsuperuser

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

run:
	$(DOCKER_COMPOSE) up --build

down:
	$(DOCKER_COMPOSE) down

shell:
	$(DOCKER_COMPOSE) exec $(SERVICE_NAME) python /app/src/manage.py shell

migrate:
	$(DOCKER_COMPOSE) exec $(SERVICE_NAME) python /app/src/manage.py migrate

createsuperuser:
	$(DOCKER_COMPOSE) exec $(SERVICE_NAME) python /app/src/manage.py createsuperuser
