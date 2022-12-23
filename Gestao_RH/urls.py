from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

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
    
    
]
