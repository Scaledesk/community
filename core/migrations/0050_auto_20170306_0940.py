# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_remove_category_categoryfk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Subcategory',
            new_name='subcategory',
        ),
        migrations.AlterField(
            model_name='category',
            name='Category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='SubCategory',
            field=models.CharField(max_length=100),
        ),
    ]
