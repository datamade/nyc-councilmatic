# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.CharField(max_length=255, unique=True, default=''),
            preserve_default=False,
        ),
    ]
