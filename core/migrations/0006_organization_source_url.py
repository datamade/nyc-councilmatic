# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_bill_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='source_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
