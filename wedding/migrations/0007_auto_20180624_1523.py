# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_auto_20180624_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='name',
            field=models.CharField(default=b'Guest', max_length=200),
        ),
    ]
