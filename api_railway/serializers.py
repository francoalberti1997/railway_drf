from rest_framework import serializers 
from . import models

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiencia
        fields = "__all__"

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proyecto
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = "__all__"

        