from django.db import models
from apps.funcionarios.models import Funcionario
from apps.empresa.models import Empresa

# Create your models here.

class Hora_extra(models.Model):
    motivo = models.CharField('Motivo',max_length=100)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT,related_name='horas_extras')
    horas = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.motivo