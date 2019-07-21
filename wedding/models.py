import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Rsvp(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_plus_one = models.BooleanField(default=False)
    attending = models.NullBooleanField()
    vegetarian_meal = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)
    def __str__ (self):
        return self.name if self.name else "Guest"

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    mailing_address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    alternate_email = models.EmailField(blank=True, null=True)
    sent_save_the_date = models.BooleanField(default=False)
    sent_invitation = models.BooleanField(default=False)
    viewed_invitation = models.BooleanField(default=False)
    sent_photos_link = models.BooleanField(default=False)
    present_comments = models.TextField(blank=True, null=True)
