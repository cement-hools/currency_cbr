from decimal import Decimal
import xml.dom.minidom as minidom
from datetime import datetime

import requests
from django.core.management import BaseCommand

from api.models import Currency


class Command(BaseCommand):
    def load_cbr(self):
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'

        resp = requests.get(url)
        doc = minidom.parseString(resp.content.decode('cp1251'))

        # Date parsing
        valcurs = doc.getElementsByTagName('ValCurs')[0]
        date_rate = valcurs.attributes.get('Date').value
        date_rate = datetime.strptime(date_rate, '%d.%m.%Y')

        # Rate parsing
        valutes = doc.getElementsByTagName('Valute')
        for item in valutes:
            code = item.attributes.get('ID').value
            num_code = item.getElementsByTagName('NumCode')[0].childNodes[0].data
            char_code = item.getElementsByTagName('CharCode')[0].childNodes[
                0].data

            nominal = item.getElementsByTagName('Nominal')[0].childNodes[0].data
            name = item.getElementsByTagName('Name')[0].childNodes[0].data
            rate = item.getElementsByTagName('Value')[0].childNodes[0].data

            nominal = int(nominal)
            rate = Decimal(rate.replace(',', '.'))

            rub_rate = rate / nominal

            currency, created = Currency.objects.get_or_create(
                name=name,
                rate=rub_rate
            )

            # try:
            #     change = rate - CurrencyRate.objects.filter(
            #         currency=currency).last().rate
            # except AttributeError:
            #     change = 0

            # course, created = CurrencyRate.objects.get_or_create(
            #     currency=currency, date_rate=date_rate,
            #     defaults={'nominal': nominal, 'rate': rate})

    def handle(self, *args, **options):
        self.load_cbr()
