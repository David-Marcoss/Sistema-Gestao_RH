import json
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView,UpdateView,ListView,DeleteView

from apps.funcionarios.models import Funcionario
from .models import Hora_extra
from .forms import HoraExtraForm
from django.contrib.auth.decorators import login_required


import xlwt    
import csv


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
    template_name = 'hora_extra/horas_extra_form.html'
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

class UtilizarHoraExtraView(View):
    
    def post(self, *args, **kwargs):

        hora_utilizada = Hora_extra.objects.get(pk=kwargs['pk'])
        horas = hora_utilizada.horas


        if hora_utilizada.horas_utilizadas:
            hora_utilizada.horas_utilizadas = False
            response =  json.dumps({"mensagem": f" {horas} utilizadas!!!"})
        else:
            hora_utilizada.horas_utilizadas = True
            response =  json.dumps({"mensagem": f" {horas} nao utilizadas!!!"})

        hora_utilizada.save()


        return HttpResponse(response,content_type = 'aplication/json')

# gera um arquivo csv com registro de horas extras
@login_required
def registro_horas_extras(request):
    
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Registro_horasEx.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['id', 'Funcionario', 'Motivo','Horas','Horas utilizadas'])

    empresa = request.user.empresa.get()
    horas = empresa.horas_extras.all()
    
    for h_ex in horas:
        horas_utilizadas = 'Não'
        if h_ex.horas_utilizadas:
            horas_utilizadas = 'Sim'

        writer.writerow([h_ex.id, h_ex.funcionario, h_ex.motivo,h_ex.horas,horas_utilizadas])

    return response


# gera um arquivo excel com registro de horas extras
class registro_horas_extras_Excel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Registro_horasEx_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['id', 'Funcionario', 'Motivo','Horas','Horas utilizadas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        empresa = request.user.empresa.get()
        registros = empresa.horas_extras.all()

        row_num = 1
        for registro in registros:
            
            horas_utilizadas = 'Não'
            if registro.horas_utilizadas:
                horas_utilizadas = 'Sim'

            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.horas, font_style)
            ws.write(row_num, 4, horas_utilizadas, font_style)
            row_num += 1

        wb.save(response)

        return response