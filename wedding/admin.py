from django.contrib import admin

from .models import Rsvp, UserProfile
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "mailing_address", "comments", "viewed_invitation", "sent_invitations")
    model = UserProfile


class RsvpAdmin(admin.ModelAdmin):
	list_display = ("guest_name", "attending")
	def guest_name(self, obj):
		return obj.name if obj.name else "Guest"

	guest_name.short_description = 'Name'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'last_login')
    list_filter = ('last_login',)
    date_hierarchy = 'last_login'

    def display_name(self, obj):
        display_name = obj.first_name
        if obj.last_name:
            display_name += obj.last_name
        return display_name
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Rsvp, RsvpAdmin)