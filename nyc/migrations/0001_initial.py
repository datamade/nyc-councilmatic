# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocd_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('classification', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=None)),
                ('date_updated', models.DateTimeField(default=None)),
                ('source_url', models.CharField(max_length=255)),
                ('source_note', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocd_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('headshot', models.CharField(max_length=255)),
            ],
        ),
    ]
