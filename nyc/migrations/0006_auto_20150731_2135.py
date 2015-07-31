# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0005_organization_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='name',
            field=models.TextField(),
        ),
    ]
