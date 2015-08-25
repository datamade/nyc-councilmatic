# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0015_auto_20150825_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legislativesession',
            name='organization',
        ),
        migrations.AddField(
            model_name='legislativesession',
            name='jurisdiction_ocd_id',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
