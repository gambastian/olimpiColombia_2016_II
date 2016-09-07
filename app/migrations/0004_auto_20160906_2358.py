# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 04:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_evento_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportista',
            name='urlImagen',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre de usuario debe ser Alfabetico', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator(code='invalid_email', message='El email no es valido')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre de usuario debe ser Alfabetico', regex='^[a-zA-Z]*$')]),
        ),
    ]
