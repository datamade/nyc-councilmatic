# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150917_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='abstract',
            field=models.TextField(blank=True),
        ),
    ]
