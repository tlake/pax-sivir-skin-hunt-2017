# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkinCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=63)),
                ('claimed', models.BooleanField(default=False)),
                ('human_name', models.CharField(default='', max_length=63)),
                ('summoner_name', models.CharField(default='', max_length=63)),
            ],
        ),
    ]
