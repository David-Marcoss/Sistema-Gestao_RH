from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import AbstractUser,User
from django.urls import reverse_lazy
from .forms import UserCreationForm

@login_required
def homeView(request):
      
    return render(request,template_name='home.html')


class cadastroview(CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Usuario'
        context['botao'] = 'Cadastrar'

        return context