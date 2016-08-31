# -*- encoding: utf-8 -*-
from django.conf.urls import url
from search import views

default_app_config = 'search.apps.SearchConfig'

urlpatterns = [
    url(r'^$', views.SearchPage.as_view(), name='search'),
]

urls = (urlpatterns, 'search', 'search')
