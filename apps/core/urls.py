from django.urls import include, path
from .views import homeView,cadastroview

urlpatterns = [
    path('',homeView,name='home'),
    path('cadastro/',cadastroview.as_view(),name='cadastro'),
    
]
