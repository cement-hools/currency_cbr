from django.contrib import admin

from api.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
