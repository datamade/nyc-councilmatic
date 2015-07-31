# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0006_auto_20150731_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='bill',
            field=models.ForeignKey(related_name='actions', to='nyc.Bill', null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='organization',
            field=models.ForeignKey(related_name='actions', to='nyc.Organization', null=True),
        ),
    ]
