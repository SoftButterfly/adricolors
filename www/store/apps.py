from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'
    verbose_name = _('Store site')

    label = 'store'
