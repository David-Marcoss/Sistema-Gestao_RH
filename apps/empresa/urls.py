from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar/',CadastroEmpresaView.as_view(),name='cadastrar-empresa'),
    path('editar/<int:pk>',UpdateEmpresaView.as_view(),name='editar-empresa'),
    path('lista-funcionarios',ListFuncionarioView.as_view(),name='list-funcionarios'),
    path('relatorio-funcionarios',relatorio_funcionarios,name='relatorio-funcionarios'),
    path('relatorio-departamentos',relatorio_departamentos.as_view(),name='relatorio-departamentos'),
    path('lista-departamentos/',ListDepartamentosView.as_view(),name='list-departamentos'),
    path('relatorio-departamentos-email',Enviar_relatorio_departamentos_email,name='relatorio-departamentos-email'),

    
]
