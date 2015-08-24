# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0012_auto_20150819_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='ocd_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bill',
            name='slug',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ocd_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='ocd_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='ocd_id',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
