from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'search'
    verbose_name = _('Search site')

    label = 'search'
