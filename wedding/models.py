import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Rsvp(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_plus_one = models.BooleanField(default=False)
    attending = models.NullBooleanField()

    def __str__ (self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    mailing_address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
