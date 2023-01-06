from django.shortcuts import render
from .models import Documento
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from apps.funcionarios.models import Funcionario

# Create your views here.


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao','arquivo']
    template_name = 'form.html'

    def form_valid(self,form):
              
        documento = form.save(commit= False)
        documento.usuario = Funcionario.objects.get(id=self.kwargs['pk'])
        documento.save()

        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Documento'
        context['botao'] = 'Cadastrar'   

        return context

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    