from django.contrib import admin

from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
	list_display = ("name", "attending")

admin.site.register(Rsvp, RsvpAdmin)