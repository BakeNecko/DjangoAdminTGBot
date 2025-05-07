# Django Telegram Notification Bot

## Описание проекта

Этот проект представляет собой веб-приложение на Django, использующее PostgreSQL в качестве базы данных. Приложение отправляет уведомления в Telegram, когда пользователь входит в админ-панель Django. Пользователи могут подписываться и отписываться от уведомлений через Telegram.

BotLink: `https://t.me/DjangoAdminBakeNeckoTestBot`

## Технологии

- Django
- PostgreSQL
- Docker
- pytelegrambotapi

## Тесты
- Не успел, поэтому проверял эмпирически. 

## Установка и запуск

### Требования

- Docker - 28.0.4
- Docker Compose - v2.34.0

### Запуск приложения в ручном режиме
1. `docker-compose up --build`
2. `docker-compose exec web python src/manage.py migrate` (Опционально) 
3. `docker-compose exec web python /app/src/manage.py createsuperuser`
4. Общаемся с ботом.

### Запуск с исп. Makefile
1. `make run`
2. `make migrate` (Опционально)
3. `make createsuperuser`
4. Общаемся с ботом

----
P.S Миграции должны выполняться в рамках команды (command) файла supervisord.conf с исп. &&