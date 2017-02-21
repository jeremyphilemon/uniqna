# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20170215_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(choices=[('SCSE', 'SCSE'), ('SENSE', 'SENSE'), ('SAS', 'SAS'), ('SELECT', 'SELECT'), ('SMBS', 'SMBS'), ('VITBS', 'VITBS'), ('VITSOL', 'VITSOL'), ('VFIT', 'VFIT'), ('V-SPARC', 'V-SPARC'), ('SBST', 'SBST'), ('SCALE', 'SCALE'), ('SCOPE', 'SCOPE'), ('SITE', 'SITE'), ('SMEC', 'SMEC'), ('SSL', 'SSL'), ('LAW', 'LAW')], default='SCSE', max_length=6),
        ),
    ]
