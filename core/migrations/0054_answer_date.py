# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_answer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
