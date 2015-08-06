# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0008_auto_20150806_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='start_date',
        ),
    ]
