# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0019_auto_20150903_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ocd_id', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100)),
                ('location_name', models.CharField(max_length=255)),
                ('location_url', models.CharField(blank=True, max_length=255)),
                ('source_url', models.CharField(max_length=255)),
                ('source_note', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('document', models.ForeignKey(to='nyc.Document', related_name='events')),
                ('event', models.ForeignKey(to='nyc.Event', related_name='documents')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('note', models.TextField()),
                ('entity_name', models.CharField(max_length=255)),
                ('entity_type', models.CharField(max_length=100)),
                ('event', models.ForeignKey(to='nyc.Event', related_name='participants')),
            ],
        ),
    ]
