# -*- encoding: utf-8 -*-
from django.conf.urls import url
from store import views

default_app_config = 'store.apps.StoreConfig'

urlpatterns = [
    url(r'^$', views.StorePage.as_view(), name='store'),
]

urls = (urlpatterns, 'store', 'store')
