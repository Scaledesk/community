# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20170306_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(default='sdffs', upload_to='documents/'),
            preserve_default=False,
        ),
    ]
