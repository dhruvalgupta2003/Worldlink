# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldlink', '0009_auto_20170829_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
