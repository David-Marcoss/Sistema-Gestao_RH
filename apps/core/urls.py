from django.urls import path
from .views import homeView,cadastroview

urlpatterns = [
    path('',homeView,name='home'),
    path('cadastro/',cadastroview.as_view(),name='cadastro'),
    
]
