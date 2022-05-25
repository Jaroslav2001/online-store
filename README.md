# Online Store (service api)

## Возможности сервиса
* Подерживает CRUD операции
* Подерживает уравление прав и доступ к url api

## Данные сервиса
* Товары
* Категории
* Свойства товаров

## Установка сервиса
`docker-compose up --build -d`

## Миграция базы данных
* Данные команды выполняются в сервисе`web`
* `python manage.py migrate`

## Создание суперпользователя
* `python manage.py createsuperuser`