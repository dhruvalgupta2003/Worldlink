# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldlink', '0002_profile_model_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='model_pic',
        ),
    ]
