# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0003_auto_20150729_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='organization',
            field=models.ForeignKey(related_name='actions', to='nyc.Organization'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(related_name='bills', to='nyc.Organization', null=True),
        ),
    ]
