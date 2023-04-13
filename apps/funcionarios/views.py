from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Empresa
from .forms import FuncionarioForm
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import User

from .api.serializers import FuncionarioSerializer 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UpdateFuncionarioView(UpdateView):
    template_name = 'form_funcionario.html'
    model = Funcionario
    form_class = FuncionarioForm
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['funcionario_id'] = self.kwargs['pk']
        context['titulo'] = 'Editar Funcionario'
        context['botao'] = 'Salvar alterações'

        return context
    
    def get_form_kwargs(self):
        kwargs = super(UpdateFuncionarioView,self).get_form_kwargs()
        kwargs.update({'empresa':self.request.user.empresa.get()})
        
        return kwargs

class DeletFuncionarioView(DeleteView):
    template_name = 'form.html'
    model = Funcionario
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o Funcionario?'
        context['botao'] = 'Confirmar'

        return context

class CreateFuncionarioView(CreateView):
    template_name = 'form.html'
    form_class = FuncionarioForm

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Funcionario'
        context['botao'] = 'Cadastrar'   

        return context

    def form_valid(self, form):
        
        funcionario = form.save(commit= False)
        funcionario.empresa = self.request.user.empresa.get()
        user = User.objects.create(username=funcionario.nome.replace(' ',''))
        funcionario.user = user
        funcionario.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    

    #esta função serve para passar um parametro extra para o formulario
    def get_form_kwargs(self):
        kwargs = super(CreateFuncionarioView,self).get_form_kwargs()
        kwargs.update({'empresa':self.request.user.empresa.get()})
        
        return kwargs


# ViewSets define the view behavior.
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


