# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-22 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0011_auto_20180707_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sent_invitation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='viewed_invitation',
            field=models.BooleanField(default=False),
        ),
    ]
