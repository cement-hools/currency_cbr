from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    """Модель валюты."""
    name = models.CharField('Name', max_length=255)
    rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.rate} руб.'
