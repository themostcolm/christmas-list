# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 07:05
from __future__ import unicode_literals

import christmas.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0005_auto_20171208_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.CharField(default=christmas.helpers.random_alpha_numeric, max_length=15),
        ),
    ]
