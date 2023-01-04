from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Empresa
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import User


class UpdateFuncionarioView(UpdateView):
    template_name = 'form_funcionario.html'
    model = Funcionario
    fields = ['nome','departamento']
    
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

        if self.kwargs['pk'] != self.request.user.funcionario.id:
            return self.request.GET.get('next', reverse_lazy('home'))
        else:
            return reverse_lazy('home')
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o Funcionario?'
        context['botao'] = 'Confirmar'

        return context

class CreateFuncionarioView(CreateView):
    template_name = 'form.html'
    model = Funcionario
    fields = ['nome','departamento'] 

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Funcionario'
        context['botao'] = 'Cadastrar'   

        return context

    def form_valid(self, form):
        
        funcionario = form.save(commit= False)
        funcionario.empresa = self.request.user.funcionario.empresa
        user = User.objects.create(username=funcionario.nome.replace(' ',''))
        funcionario.user = user
        funcionario.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
   


