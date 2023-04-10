from django.urls import path
from .views import list_bancohoras,CreateHoraExtraView,EditHoraExtraView,DeleteHoraExtraView,UtilizarHoraExtraView

urlpatterns = [
    path('banco-horas/',list_bancohoras,name='banco-horas'),
    path('cadastrar-horas-extra/',CreateHoraExtraView.as_view(),name='create-hora-extra'),
    path('Editar-horas-extra/<int:pk>/',EditHoraExtraView.as_view(),name='edit-horas-extras'),
    path('Utilizar-horas-extra/<int:pk>/',UtilizarHoraExtraView.as_view(),name='utilizar-horas-extras'),
    path('Excluir-horas-extra/<int:pk>/',DeleteHoraExtraView.as_view(),name='delete-horas-extras'),
]
