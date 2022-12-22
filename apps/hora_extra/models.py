from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.

class Hora_extra(models.Model):
    motivo = models.CharField('Motivo',max_length=100)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo