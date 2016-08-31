from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    verbose_name = _('Home site')

    label = 'home'
