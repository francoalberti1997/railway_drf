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

    
    # def retrieve(self, request, *args, **kwargs):
    #     # Tu lógica personalizada aquí para obtener un único objeto


    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
       
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
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

    # def retrieve(self, request, *args, **kwargs):
    #     # Tu lógica personalizada aquí para obtener un único objeto


    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
       
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
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

    def get_permissions(self):
        if self.action == 'list' and not self.request.user.is_authenticated:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()
    
    # def retrieve(self, request, *args, **kwargs):
    #     # Tu lógica personalizada aquí para obtener un único objeto


    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
       
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAdminUser]  # Solo permite a los administradores

    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  # Hereda el comportamiento original
        
    def list(self,request, *args, **kwargs):
        if request.user.is_staff:  
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)                
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


def login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_staff:
                login(request, user)
                contactos = Contacto.objects.all()

                # Redirige o renderiza la página con los datos permitidos para el admin
                return render(request, 'admin_data.html', {'user': user, "contactos":contactos})
            else:
                return HttpResponseForbidden("No tiene permisos de administrador")
    else:
        form = AdminLoginForm()

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login_view')