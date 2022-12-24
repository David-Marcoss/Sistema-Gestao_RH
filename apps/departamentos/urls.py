from django.urls import path
from .views import UpdateDepartamentoView,DeletDepartamentoView,CreateDepartamentoView

urlpatterns = [
    path('cadastrar-departamento/',CreateDepartamentoView.as_view(),name='create-departamento'),
    path('editar-departamento/<int:pk>',UpdateDepartamentoView.as_view(),name='edit-departamento'),
    path('excluir-departamento/<int:pk>',DeletDepartamentoView.as_view(),name='delet-departamento'),
    
]
