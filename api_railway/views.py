from django.contrib.auth.models import User
from .models import *
from .serializers import ExperienciaSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes  # Añade esta línea

class UserViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_api(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        print("*")
        print(user.username)
        print("*")
    return Response(content)
