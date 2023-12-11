from django.db import models

# Create your models here.

class Experiencia(models.Model):
    trabajo = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    img = models.ImageField()
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return (self.trabajo)
