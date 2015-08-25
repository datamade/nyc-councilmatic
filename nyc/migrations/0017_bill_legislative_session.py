# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0016_auto_20150825_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(related_name='bills', to='nyc.LegislativeSession', null=True),
            preserve_default=False,
        ),
    ]
