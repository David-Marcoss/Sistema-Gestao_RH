from django.urls import path
from .views import UpdateFuncionarioView,DeletFuncionarioView,CreateFuncionarioView

urlpatterns = [
    path('cadastrar-funcionario/',CreateFuncionarioView.as_view(),name='create-funcionario'),
    path('editar-funcionario/<int:pk>',UpdateFuncionarioView.as_view(),name='edit-funcionario'),
    path('excluir-funcionario/<int:pk>',DeletFuncionarioView.as_view(),name='delet-funcionario'),
    
]
