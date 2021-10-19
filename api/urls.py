from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CurrencyViewSet

router = DefaultRouter()
router.register('currencies', CurrencyViewSet, basename='currencies')

urlpatterns = [
    path('v1/', include(router.urls)),
]
