from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

from apps.funcionarios.models import Funcionario
from .models import Hora_extra
from django.contrib.auth.decorators import login_required


@login_required
def list_bancohoras(request):
    template_name = 'hora_extra/banco_horas.html'
    empresa = request.user.funcionario.empresa
    horas = empresa.horas_extras.all()

    return render(request,template_name,context={'horas':horas,'empresa':empresa})
