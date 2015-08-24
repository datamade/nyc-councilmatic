# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0013_auto_20150824_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(to='nyc.Organization', null=True, related_name='children'),
        ),
    ]
