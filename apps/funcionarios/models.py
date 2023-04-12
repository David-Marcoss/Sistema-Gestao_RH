from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresa.models import Empresa
from django.db.models import Sum

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField('nome',max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT,related_name='funcionario')
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True,blank=True,related_name='funcionarios')
    departamento = models.ManyToManyField(Departamento,related_name='funcionarios',blank=False)

    def __str__(self):
        return self.nome
    
    @property
    def get_total_horas_ex_utilizadas(self):
        return self.horas_extras.filter(horas_utilizadas = True).aggregate(Sum('horas'))['horas__sum']
    
    @property
    def get_total_horas_ex_nao_utilizadas(self):
        return self.horas_extras.filter(horas_utilizadas = False).aggregate(Sum('horas'))['horas__sum']