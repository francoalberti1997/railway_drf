from rest_framework import serializers 
from . import models

class PropuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Propuestas
        fields = "__all__"
