# -*- encoding: utf-8 -*-
from django.conf.urls import url
from home import views

default_app_config = 'home.apps.HomeConfig'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
]

urls = (urlpatterns, 'home', 'home')
