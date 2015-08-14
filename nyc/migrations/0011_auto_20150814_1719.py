# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0010_auto_20150806_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='identifier',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
