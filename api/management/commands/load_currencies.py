import requests
from django.core.management import BaseCommand
from django.db import IntegrityError

from api.models import Currency


class Command(BaseCommand):
    def load_currencies(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = requests.get(url).json()
        currencies = data.get('Valute')
        if not currencies:
            return self.stdout.write(
                self.style.WARNING('Ошибка подключения'))

        currencies_set = Currency.objects.all()

        if currencies_set.exists():
            print('Обновление курса валют')
            for currency in currencies_set:
                char_code = currency.name.split()[-1]
                currency_data = currencies.get(char_code)
                if currency_data:
                    new_rate = currency_data.get('Value')
                    nominal = currency_data.get('Nominal', 1)
                    new_rub_rate = new_rate / nominal

                    currency.rate = new_rub_rate
            try:
                Currency.objects.bulk_update(currencies_set, ['rate'])
            except IntegrityError as err:
                self.stdout.write(
                    self.style.WARNING(f'Данные не обновлены')
                )
        else:
            print('Загрузка курса валют')
            currencies_list = []
            for currency in currencies.values():
                name = currency.get('Name')
                char_code = currency.get('CharCode')
                db_name = f'{name} {char_code}'
                rate = currency.get('Value')
                nominal = currency.get('Nominal', 1)

                rub_rate = rate / nominal

                currency = Currency(
                    name=db_name,
                    rate=rub_rate
                )
                currencies_list.append(currency)
            try:
                Currency.objects.bulk_create(currencies_list)
            except IntegrityError as err:
                self.stdout.write(
                    self.style.WARNING(f'Данные не сохранены')
                )

        self.stdout.write(self.style.SUCCESS('Курс валют успешно загружен'))

    def handle(self, *args, **options):
        self.load_currencies()
