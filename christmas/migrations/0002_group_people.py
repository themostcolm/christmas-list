# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(to='christmas.Profile'),
        ),
    ]