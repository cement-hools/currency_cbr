import requests
from django.core.management import BaseCommand
from django.db import transaction, IntegrityError

from api.models import Currency


class Command(BaseCommand):
    def load_cbr(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        data = requests.get(url).json()
        currencies = data.get('Valute')

        if not currencies:
            self.stdout.write(
                self.style.SUCCESS('Ошибка подключения'))
            return
        
        for currency in currencies.values():
            name = currency.get('Name')
            rate = currency.get('Value')
            nominal = currency.get('Nominal', 1)
            rub_rate = rate / nominal

            try:
                with transaction.atomic():
                    currency, created = Currency.objects.update_or_create(
                        name=name,
                        defaults={'rate': rub_rate},
                    )
            except IntegrityError as err:
                self.stdout.write(
                    self.style.WARNING(f'Данные для {name} не сохранены'))

        self.stdout.write(self.style.SUCCESS('Курс валют успешно сохранен'))

    def handle(self, *args, **options):
        self.load_cbr()
