from django.shortcuts import render

def departamentoView(request):
    return render(request,template_name='departamento.html')


