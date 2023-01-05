from .models import Hora_extra
from apps.funcionarios.models import Funcionario
from django import forms

class HoraExtraForm(forms.ModelForm):

    def __init__(self, empresa, *args,**kargs):
        super(HoraExtraForm,self).__init__(*args,**kargs)
        """
            perçonalizando campos do formulario para que so seja mostrados 
            funcionarios referentes a uma empresa
        """
        self.fields['funcionario'].queryset = empresa.funcionarios.all()
     
    class Meta:
          model = Hora_extra
          fields = ['motivo','funcionario','horas']