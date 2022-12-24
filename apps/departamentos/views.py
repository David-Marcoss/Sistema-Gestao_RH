from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from apps.empresa.models import Empresa
from django.contrib.auth.models import User
from .models import Departamento


class UpdateDepartamentoView(UpdateView):
    template_name = 'form.html'
    model = Departamento
    fields = ['nome']
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Departamento'
        context['botao'] = 'Salvar alterações'

        return context

class DeletDepartamentoView(DeleteView):
    template_name = 'form.html'
    model = Departamento
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
      
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o Departamento?'
        context['botao'] = 'Confirmar'

        return context

class CreateDepartamentoView(CreateView):
    template_name = 'form.html'
    model = Departamento
    fields = ['nome'] 

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Departamento'
        context['botao'] = 'Cadastrar'   

        return context

    def form_valid(self, form):
        
        departemento = form.save(commit= False)
        departemento.empresa = self.request.user.funcionario.empresa
        departemento.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
   




