# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_channel_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='color',
            field=models.CharField(default='#673AB7', max_length=30),
        ),
    ]
