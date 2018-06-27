# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_rsvp_is_plus_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
