# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0007_auto_20150731_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255, blank=True)),
                ('role', models.CharField(max_length=255, blank=True)),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('organization', models.ForeignKey(related_name='memberships', to='nyc.Organization')),
                ('person', models.ForeignKey(related_name='memberships', to='nyc.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocd_id', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('organization', models.ForeignKey(related_name='posts', to='nyc.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(related_name='memberships', to='nyc.Post', null=True),
        ),
    ]
