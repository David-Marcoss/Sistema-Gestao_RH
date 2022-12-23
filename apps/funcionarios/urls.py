from django.urls import path
from .views import UpdateFuncionarioView,DeletFuncionarioView

urlpatterns = [
    path('editar-funcionario/<int:pk>',UpdateFuncionarioView.as_view(),name='edit-funcionario'),
    path('excluir-funcionario/<int:pk>',DeletFuncionarioView.as_view(),name='delet-funcionario'),
    
]
