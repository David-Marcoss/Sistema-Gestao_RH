from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views

from apps.core.views import UserViewSet,GroupViewSet
from apps.funcionarios.views import FuncionarioViewSet
from apps.hora_extra.views import Hora_ExtraViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'horas-extras', Hora_ExtraViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('apps.core.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path("documentos/",include('apps.documentos.urls')),
    path("funcionarios/",include('apps.funcionarios.urls')),
    path("empresa/",include('apps.empresa.urls')),
    path("hora-extra/",include('apps.hora_extra.urls')),

    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token)
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)