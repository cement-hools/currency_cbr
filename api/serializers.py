from rest_framework.serializers import ModelSerializer

from api.models import Currency


class CurrencySerializer(ModelSerializer):
    """Сериалайзер валюты."""

    class Meta:
        model = Currency
        fields = '__all__'
