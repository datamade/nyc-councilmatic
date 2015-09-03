# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0018_auto_20150825_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('bill', models.ForeignKey(to='nyc.Bill', related_name='documents')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='bill',
        ),
        migrations.AddField(
            model_name='billdocument',
            name='document',
            field=models.ForeignKey(to='nyc.Document', related_name='bills'),
        ),
    ]
