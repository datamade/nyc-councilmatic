# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0011_auto_20150814_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('classification', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='slug',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='bill',
            field=models.ForeignKey(related_name='sponsorships', to='nyc.Bill'),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='person',
            field=models.ForeignKey(related_name='sponsorships', to='nyc.Person'),
        ),
    ]
