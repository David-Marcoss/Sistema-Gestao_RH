from apps.funcionarios.models import Funcionario
from django import forms

class FuncionarioForm(forms.ModelForm):

    def __init__(self, empresa, *args,**kargs):
        super(FuncionarioForm,self).__init__(*args,**kargs)
        """
            perçonalizando campos do formulario para que so seja mostrados 
            funcionarios referentes a uma empresa
        """
        self.fields['departamento'].queryset = empresa.departamentos.all()
     
    class Meta:
          model = Funcionario
          fields = ['nome','departamento'] 