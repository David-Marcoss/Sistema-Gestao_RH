from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    path('cadastrar/<int:pk>',DocumentoCreate.as_view(),name='cadastrar-documento'),
    
]
