# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20170301_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='userdipp',
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
            preserve_default=False,
        ),
    ]
