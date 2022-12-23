from django.urls import path
from .views import CadastroEmpresaView,UpdateEmpresaView,ListFuncionarioView

urlpatterns = [
    path('cadastrar/',CadastroEmpresaView.as_view(),name='cadastrar-empresa'),
    path('editar/<int:pk>',UpdateEmpresaView.as_view(),name='editar-empresa'),
    path('lista-funcionarios',ListFuncionarioView.as_view(),name='list-funcionarios'),

    
]
