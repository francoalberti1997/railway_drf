from django.db import models

# Create your models here.

class Propuestas(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField(max_length=25)
    propuesta = models.CharField(max_length=25)

    def __str__(self):
        return (self.nombre)
