# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_profile_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(default=10, to='core.Profile'),
            preserve_default=False,
        ),
    ]
