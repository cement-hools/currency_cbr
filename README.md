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

Ответ
```json

```