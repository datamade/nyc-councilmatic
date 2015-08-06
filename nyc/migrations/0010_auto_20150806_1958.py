# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0009_auto_20150806_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
        migrations.AddField(
            model_name='person',
            name='source_note',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='source_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
