# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='needSupport',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='provideSupport',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
