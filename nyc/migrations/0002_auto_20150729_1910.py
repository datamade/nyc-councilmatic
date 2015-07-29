# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date_updated',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='source_note',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='headshot',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
