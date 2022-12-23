from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Empresa
from apps.funcionarios.models import Funcionario


class UpdateFuncionarioView(UpdateView):
    template_name = 'form.html'
    model = Funcionario
    fields = ['nome']
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Funcionario'
        context['botao'] = 'Salvar alterações'

        return context

class DeletFuncionarioView(DeleteView):
    template_name = 'form.html'
    model = Funcionario
    
    def get_success_url(self):

        if self.kwargs['pk'] != self.request.user.id:
            return self.request.GET.get('next', reverse_lazy('home'))
        else:
            return reverse_lazy('home')
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o Funcionario?'
        context['botao'] = 'Confirmar'

        return context