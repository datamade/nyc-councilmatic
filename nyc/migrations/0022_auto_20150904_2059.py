# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0021_actionrelatedentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionrelatedentity',
            name='organization_ocd_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='actionrelatedentity',
            name='person_ocd_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
