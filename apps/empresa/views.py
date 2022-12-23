from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView
from .models import Empresa
from apps.funcionarios.models import Funcionario


class CadastroEmpresaView(CreateView):
    template_name = 'form.html'
    model = Empresa
    fields = ["nome"]

    def form_valid(self, form):
        form.save()
        
        self.request.user.funcionario.empresa = form.instance

        self.request.user.funcionario.save()
        
        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Empresa'
        context['botao'] = 'Cadastrar'

        return context
        
    success_url = reverse_lazy('home')



class UpdateEmpresaView(CreateView):
    template_name = 'form.html'
    model = Empresa
    fields = ["nome"]

    success_url = reverse_lazy('home')

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Empresa'
        context['botao'] = 'Salvar alterações'

        return context


class ListFuncionarioView(ListView):
    template_name = 'empresa/list_funcionarios.html'    
    model= Funcionario

    def get_queryset(self):
        
        if self.request.user.funcionario:
            
            empresa = self.request.user.funcionario.empresa

            return empresa.funcionarios.all()
        else:
             return None


