# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NYCBill',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('councilmatic_core.bill',),
        ),
    ]
