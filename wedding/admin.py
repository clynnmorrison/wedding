from django.contrib import admin

from .models import Rsvp


class RsvpAdmin(admin.ModelAdmin):
	list_display = ("guest_name", "attending")

	def guest_name(self, obj):
		return obj.name if obj.name else "Guest"

	guest_name.short_description = 'Name'

admin.site.register(Rsvp, RsvpAdmin)