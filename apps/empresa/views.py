from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView,UpdateView,ListView
from .models import Empresa
from apps.funcionarios.models import Funcionario
from apps.departamentos.models import Departamento

from django.contrib.auth.decorators import login_required

import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa




class CadastroEmpresaView(CreateView):
    template_name = 'form.html'
    model = Empresa
    fields = ["nome"]

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.dono = self.request.user
        form.save()
        
        return super().form_valid(form)
    
    def get_context_data(self, *args,**kwargs):

        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Cadastrar Empresa'
        context['botao'] = 'Cadastrar'

        return context
        
    success_url = reverse_lazy('home')



class UpdateEmpresaView(UpdateView):
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
        
        empresa = self.request.user.empresa.get()

        if empresa:

            return empresa.funcionarios.all()
        else:
             return None

class ListDepartamentosView(ListView):
    template_name = 'departamentos/list_departamentos.html'    
    model= Departamento

    def get_queryset(self):
        
        empresa = self.request.user.empresa.get()

        if empresa:

            return empresa.departamentos.all()
        else:
             return None


    
#Gerando relatorio com a biblioteca reportlab
@login_required
def relatorio_funcionarios(request):
    response = HttpResponse(content_type = 'aplication/pdf')
    response['Content_Disposition'] = 'attachment; filename = "relarorio.pdf"'

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(200, 810, "Relatorio de Funcionarios")
    p.drawString(0, 800, "_"*150)

    y = 780

    empresa = request.user.empresa.get()

    for funcionario in empresa.funcionarios.all():
        p.drawString(10, y, f"Nome: {funcionario.nome} - Departamento: {funcionario.departamento.get()}")
        y -= 30


    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


#Gera um pdf atravez de um template html
class relatorio_departamentos(View):


    def get(self, request):
        empresa = self.request.user.empresa.get()

        params = {
            'departamentos': empresa.departamentos.all(),
            'empresa': empresa,
        }
        return Render.render('empresa/relatorio.html', params, 'relatorio')