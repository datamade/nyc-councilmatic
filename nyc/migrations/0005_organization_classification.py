# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0004_auto_20150731_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='classification',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
