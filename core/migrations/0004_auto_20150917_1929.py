# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150915_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='website_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
