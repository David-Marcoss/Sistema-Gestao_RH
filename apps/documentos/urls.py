from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    path('cadastrar/',DocumentoCreate.as_view(),name='cadastrar-documento'),
    
]
