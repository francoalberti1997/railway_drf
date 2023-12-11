from django.contrib import admin
from django.urls import path, include 
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'experiencia', views.UserViewSet)
# Si tienes más vistas, las registras aquí
# router.register(r'otra', views.OtraVistaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('get/', views.get_api),
    # Otras URL o inclusiones aquí si es necesario
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



