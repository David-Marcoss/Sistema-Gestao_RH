from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresa.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField('nome',max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT,related_name='funcionario')
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True,blank=True,related_name='funcionarios')
    departamento = models.ManyToManyField(Departamento,related_name='funcionarios')

    def __str__(self):
        return self.nome