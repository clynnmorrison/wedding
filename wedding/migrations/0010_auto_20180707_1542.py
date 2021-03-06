# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0009_rsvp_vegetarian_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='is_child',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='alternate_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
