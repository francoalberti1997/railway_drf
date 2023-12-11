from rest_framework import serializers 
from . import models

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiencia
        fields = "__all__"
