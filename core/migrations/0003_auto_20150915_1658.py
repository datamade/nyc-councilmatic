# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaItemBill',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
                ('description', models.TextField()),
                ('event', models.ForeignKey(related_name='agenda_items', to='core.Event')),
            ],
        ),
        migrations.AddField(
            model_name='agendaitembill',
            name='agenda_item',
            field=models.ForeignKey(related_name='related_bills', to='core.EventAgendaItem'),
        ),
        migrations.AddField(
            model_name='agendaitembill',
            name='bill',
            field=models.ForeignKey(related_name='related_agenda_items', to='core.Bill'),
        ),
    ]
