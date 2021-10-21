# currency_cbr
Загрузка данных о курсе валют и выдача резудьтата через API

### Технологии
Python, Django, DRF, PostgreSQL

### Описание

- Источник для получения курса валют
```
https://www.cbr-xml-daily.ru/daily_json.js
```
- Загрузит/обновить таблицу курса валют
```
python manage.py load_currencies
```

- **GET**```/api/v1/currencies/``` Показать все записи из таблицы курса волют. 
10 объектов на странице, параметр страницы ```page```

Ответ
```json
{
    "count": 34,
    "next": "http://127.0.0.1:8000/api/v1/currencies/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Австралийский доллар",
            "rate": "53.1292"
        },
      ...
```

- **GET**```/api/v1/currencies/{currency_id/``` Показать курс для  переданого id. (REST frendly)

Ответ
```json
{
    "id": 11,
    "name": "Доллар США",
    "rate": "70.9904"
}
```
- **GET**```/api/v1/currency/{currency_id/``` Показать курс для  переданого id. (так как было в тз. полностью повторяет ```/api/v1/currencies/{currency_id/```)

## Установка и запуск на сервере разработчика
1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/currency_cbr
    ```
2. Перейдите в директорию currency_cbr
    ```
   cd currency_cbr
    ```
3. Создать виртуальное окружение, активировать и установить зависимости
    ``` 
   python -m venv venv
    ```
   Варианты активации окружения:
   - windows ``` venv/Scripts/activate ```
   - linux ``` venv/bin/activate ```
     <br><br>
   ```
   python -m pip install -U pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Выполните миграции
   ```
   python manage.py migrate
   ```
4. Загрузить курс валют
   ```
   python manage.py load_currencies
   ```
5. Создать супер юзера
   ```
   python manage.py createsuperuser
   ```
6. Запустить приложение на сервере разработчика
   ```
   python manage.py runserver
   ```
7. Проект доступен 
   ```
   http://127.0.0.1:8000/
   http://localhost:8000/
   ```

## Запуск в трех контейнерах (PostgreSQL, Web, Nginx)

1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/currency_cbr
    ```
2. Перейдите в директорию currency_cbr
    ```
   cd currency_cbr
    ```
3. Запустить docker-compose
    ```
    docker-compose up --build
    ```
4. Зайти в контейнер и выполнить миграции
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
5. Зайти в контейнер и выполнить миграции
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
6. Зайти в контейнер и выполнить загрузку курса валют.
    ```
    docker-compose exec web python manage.py load_currencies
    ```
7. Проект доступен 
   ```
   http://127.0.0.1/
   http://localhost/
   ```


