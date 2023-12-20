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
router_otra = routers.DefaultRouter()
router_otra.register(r'proyecto', views.UserViewSet_proyectos)

router_skill = routers.DefaultRouter()
router_skill.register(r'skills', views.UserViewSet_skills)

router_contacto = routers.DefaultRouter()
router_contacto.register(r'contacto', views.UserViewSet_contacto)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(router_otra.urls)),
    path('api/', include(router_skill.urls)),
    path('api/', include(router_contacto.urls)),
    path('login/', views.login_view, name='login_view'),
    # path('logout/', views.logout_view, name='logout_view'),


    # Otras URL o inclusiones aquí si es necesario
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#python manage.py migrate
#python manage.py makemigrations
#python manage.py runserver

