# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0020_event_eventdocument_eventparticipant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRelatedEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('entity_type', models.CharField(max_length=100)),
                ('entity_name', models.CharField(max_length=255)),
                ('organization_ocd_id', models.CharField(max_length=100)),
                ('person_ocd_id', models.CharField(max_length=100)),
                ('action', models.ForeignKey(to='nyc.Action', related_name='related_entities')),
            ],
        ),
    ]
