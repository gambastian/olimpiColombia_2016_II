# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_deporte_urlimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
