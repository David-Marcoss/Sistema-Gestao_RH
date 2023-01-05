from django.shortcuts import render,redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

from apps.funcionarios.models import Funcionario
from .models import Hora_extra
from .forms import HoraExtraForm
from django.contrib.auth.decorators import login_required


@login_required
def list_bancohoras(request):
    template_name = 'hora_extra/banco_horas.html'
    empresa = request.user.empresa.get()
    horas = empresa.horas_extras.all()

    return render(request,template_name,context={'horas':horas,'empresa':empresa})

class CreateHoraExtraView(CreateView):
    template_name = 'form.html'
    form_class = HoraExtraForm

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar hora extra'
        context['botao'] = 'Cadastrar'   

        return context

    def form_valid(self, form):
        
        departemento = form.save(commit= False)
        departemento.empresa = self.request.user.empresa.get()
        departemento.save()

        return super().form_valid(form)
    
    #esta função serve para passar um parametro extra para o formulario
    def get_form_kwargs(self):
        kwargs = super(CreateHoraExtraView,self).get_form_kwargs()
        kwargs.update({'empresa':self.request.user.empresa.get()})
        
        return kwargs
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('home'))
    
   

class EditHoraExtraView(UpdateView):
    template_name = 'form.html'
    model = Hora_extra
    fields = ['motivo','funcionario','horas']  

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Editar Horas Extras'
        context['botao'] = 'Salvar alterações'

        return context
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('banco-horas'))


class DeleteHoraExtraView(DeleteView):
    template_name = 'form.html'
    model = Hora_extra
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('banco-horas'))
      
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Deseja Excluir o registro de hoas extras?'
        context['botao'] = 'Confirmar'

        return context
