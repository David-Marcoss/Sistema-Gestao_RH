from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField('Descricao',max_length=80)
    usuario = models.ForeignKey(Funcionario,on_delete=models.PROTECT,related_name='documentos')
    arquivo =  models.FileField(upload_to='media/documents')


    def __str__(self):
        return self.descricao