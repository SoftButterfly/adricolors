# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView


class StorePage(TemplateView):
    template_name = "StorePage.html"
