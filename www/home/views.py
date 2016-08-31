# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "HomePage.html"
