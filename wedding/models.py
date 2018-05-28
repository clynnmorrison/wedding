import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Rsvp(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    attending = models.NullBooleanField ()
	
    def __str__ (self):
        return self.name