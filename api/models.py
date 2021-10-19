from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    name = models.CharField('Name', max_length=255)
    # code = models.SlugField(unique=True)
    # num_code = models.SlugField()
    # char_code = models.SlugField()
    rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=4)


    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        ordering = ['name']

    def __str__(self):
        return self.name


# class CurrencyRate(models.Model):
#     currency = models.ForeignKey(Currency, verbose_name=_('Currency'))
#     date_rate = models.DateField(_('Date of rate'), db_index=True)
#     nominal = models.PositiveSmallIntegerField(_('Nominal'))
#     rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=4)
#     # change = models.DecimalField(_('Change'), max_digits=10, decimal_places=4)
#
#     class Meta:
#         verbose_name = _('Rate of currency')
#         verbose_name_plural = _('Rates of currency')
#         ordering = ['date_rate']
#
#     def __str__(self):
#         return '{} - {}'.format(self.date_rate, self.rate)

