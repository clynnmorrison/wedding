# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_auto_20180624_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='is_plus_one',
            field=models.BooleanField(default=False),
        ),
    ]
