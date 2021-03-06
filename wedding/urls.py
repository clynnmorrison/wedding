# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

import spirit.urls

# Override admin login for security purposes
from django.contrib.auth.decorators import login_required
from wedding import views
from django.views.generic import TemplateView
admin.site.login = login_required(admin.site.login)


urlpatterns = [
    #url(r'^song-requests/', TemplateView.as_view(template_name='wedding/song_requests.html')),
    url(r'^suggestions', views.suggestions),
    url(r'^suggest', views.suggest),
    url(r'^rsvp', views.rsvp, name="rsvp"),
    url(r'^question-forum', include(spirit.urls)),
    url(r'invitation', TemplateView.as_view(template_name='wedding/invitation.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user-images/(?P<user_id>\d+)/letter.jpg', views.invitation_envelope_image),
    url(r'^', views.render_wedding_woo, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
