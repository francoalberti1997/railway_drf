from django.db import models

# Create your models here.

class Experiencia(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    img = models.ImageField()
    descripcion = models.CharField(max_length=200)
    puesto = models.CharField(max_length=25)

    def __str__(self):
        return (self.nombre)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    img = models.ImageField()
    motivacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=25)

    def __str__(self):
        return (self.nombre)


class Skills(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    img = models.ImageField()

    def __str__(self):
        return (self.nombre)

