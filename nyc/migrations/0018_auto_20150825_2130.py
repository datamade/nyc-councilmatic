# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0017_bill_legislative_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('note', models.TextField()),
                ('url', models.TextField()),
                ('bill', models.ForeignKey(related_name='documents', to='nyc.Bill')),
            ],
        ),
        migrations.RemoveField(
            model_name='documents',
            name='bill',
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
    ]
