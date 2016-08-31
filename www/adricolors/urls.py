# -*- encoding: utf-8 -*-
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
import home
import search
import store

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include(search.urls)),
    url(r'^store/', include(store.urls)),
    url(r'^', include(home.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
