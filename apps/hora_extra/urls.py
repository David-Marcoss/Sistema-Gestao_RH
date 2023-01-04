from django.urls import path
from .views import list_bancohoras

urlpatterns = [
    path('banco-horas/',list_bancohoras,name='banco-horas'),
    
]
