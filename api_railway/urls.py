from django.contrib import admin
from django.urls import path, include 
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'propuestas', views.UserViewSet)
# Si tienes más vistas, las registras aquí
# router.register(r'otra', views.OtraVistaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Otras URL o inclusiones aquí si es necesario
]

