from django.urls import path
from .views import departamentoView

urlpatterns = [
    path('view/',departamentoView,name='departamento'),
    
]
