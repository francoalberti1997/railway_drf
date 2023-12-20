from django.contrib.auth.models import User
from .models import *
from .serializers import ExperienciaSerializer, ProyectoSerializer, SkillSerializer, ContactoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes  # Añade esta línea
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

    
    def retrieve(self, request, *args, **kwargs):
        # Tu lógica personalizada aquí para obtener un único objeto
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().create(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    
    def put(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().put(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def delete(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().delete(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().destroy(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().retrieve(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

class UserViewSet_proyectos(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    def retrieve(self, request, *args, **kwargs):
        # Tu lógica personalizada aquí para obtener un único objeto


        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().create(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def put(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().put(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def delete(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().delete(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    
    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().destroy(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().retrieve(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
    )
class UserViewSet_skills(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
 
    def create(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().create(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

    def put(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().put(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def delete(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().delete(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().retrieve(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )
    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:  # Verifica si el usuario no es un administrador
            return super().destroy(request, *args, **kwargs)  # Hereda el comportamiento original
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

class UserViewSet_contacto(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]  # Solo permite a los administradores

    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)  # Hereda el comportamiento original
        
    def list(self,request, *args, **kwargs):
        print(request.user)
            
        if request.user.is_staff:  
            print(request.user)
            return super().list(request, *args, **kwargs)               
        else:
            return Response({"mensaje": "No tiene permisos"}, status=status.HTTP_403_FORBIDDEN) 

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_staff:  
            return super().retrieve(request, *args, **kwargs)  
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:  
            return super().update(request, *args, **kwargs)  
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:  
            return super().destroy(request, *args, **kwargs)  
        else:
            return Response(
                {"mensaje": "No tienes permiso para realizar esta acción"},
                status=status.HTTP_403_FORBIDDEN
            )

from rest_framework.decorators import api_view
from rest_framework.response import Response




from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from api_railway.forms import AdminLoginForm
from django.http import HttpResponseForbidden, JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # username = data.get('username')
        # password = data.get('password')
        # form = AdminLoginForm(data)
        print(data)
        try:
            user = authenticate(username=data["username"], password=data["password"])
        except:
            print("except Datos de formulario no válidos")
            return JsonResponse({"error": "Datos de formulario no válidos"}, status=100)
        
        if user and user.is_staff:
            print(f"se logueo parece. Enviara {user} y la request es: {request}")
            login(request, user)
            contactos = Contacto.objects.all()
            # response = requests.get('http://localhost:8000/api/contacto/')
            
            # Devolver la respuesta al frontend como JSON
            serializer = ContactoSerializer(contactos, many=True)
            contactos_serializados = serializer.data

            return JsonResponse({"user": user.username, "contacto":contactos_serializados}, status=200)
        
        else:
            print(f"el user es: {user}")
            return JsonResponse({"error": "Datos de formulario no válidos"}, status=400)
    else:
        return HttpResponseForbidden("Acceso prohibido")


from django.contrib.auth import logout
from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('login_view')