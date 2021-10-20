from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Currency
from api.serializers import CurrencySerializer


class CurrencyViewSet(ReadOnlyModelViewSet):
    """Список валют и просмотр отдельной валюты."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
