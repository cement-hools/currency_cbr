from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CurrencyViewSet

router = DefaultRouter()
router.register('currencies', CurrencyViewSet, basename='currencies')

currency_retrieve = CurrencyViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/currency/<int:pk>/', currency_retrieve, name='currency_retrieve'),
]
