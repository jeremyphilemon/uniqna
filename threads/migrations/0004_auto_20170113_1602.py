# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_answer_answer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_author',
            field=models.CharField(default='anon', max_length=100, verbose_name='Author'),
        ),
    ]
