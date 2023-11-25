from django.contrib.auth.models import User
from .models import *
from .serializers import PropuestasSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = Propuestas.objects.all()
    serializer_class = PropuestasSerializer