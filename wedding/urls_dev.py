# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from wedding import views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^song-requests/', TemplateView.as_view(template_name='wedding/song_requests.html')),
    url(r'^suggestions', views.suggestions),
    url(r'^suggest', views.suggest),
    url(r'^', views.render_wedding_woo),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)