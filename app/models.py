from __future__ import unicode_literals
<<<<<<< HEAD

=======
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
>>>>>>> refs/remotes/origin/master
from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=8,null=False)
<<<<<<< HEAD
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
=======
    nombre = models.CharField(max_length=50,null=False,  validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='El nombre de usuario debe ser Alfabetico',
            code='invalid_nombre'
        ),
    ])
    apellido = models.CharField(max_length=50,null=False, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='El nombre de usuario debe ser Alfabetico',
            code='invalid_nombre'
        ),
    ])
    email = models.EmailField(max_length=50,null=False, validators=[
        EmailValidator(message='El email no es valido', code = 'invalid_email')
        ])
>>>>>>> refs/remotes/origin/master
    

class Deportista(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    lugar_nacimiento = models.CharField(max_length=50,null=False)
    fecha_nacimiento = models.DateField(null=False)
    edad = models.IntegerField(null=False)
    peso = models.FloatField(null=False)
    estatura = models.FloatField(null=False)
    nombre_entrenador = models.CharField(max_length=80,null=False)

class Destacado(models.Model):
    deportista = models.ForeignKey(Deportista, null=False)
    video = models.CharField(max_length=100,null=False)

class Deporte(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    urlImagen = models.CharField(max_length=1000,null=True)

class Deporte_Deportista(models.Model):
    deportista = models.ForeignKey(Deportista, null=False)
    deporte = models.ForeignKey(Deporte, null=False)

class Evento(models.Model):
<<<<<<< HEAD
    fecha = models.DateTimeField
=======
    fecha = models.DateTimeField()
>>>>>>> refs/remotes/origin/master
    modalidad = models.ForeignKey(Deporte, null=False)
    deportista = models.ForeignKey(Deportista, null=False)
    resultado = models.CharField(max_length=100,null=False)
