# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyc', '0014_organization_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('note', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(related_name='legislative_sessions', to='nyc.Organization')),
            ],
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='name',
            new_name='description',
        ),
        migrations.AddField(
            model_name='action',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='full_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='last_action_date',
            field=models.DateTimeField(null=True, default=None),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documents',
            name='bill',
            field=models.ForeignKey(related_name='documents', to='nyc.Bill'),
        ),
    ]
