from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination, \
    PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.models import Currency
from api.serializers import CurrencySerializer


class CurrencyViewSet(ModelViewSet):
    """."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # pagination_class = PageNumberPagination
    # PageNumberPagination.page_size = 10

