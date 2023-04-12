from django.db import models
from apps.empresa.models import Empresa


class Departamento(models.Model):
    nome = models.CharField('nome',max_length=100)
    empresa = models.ForeignKey(Empresa,related_name='departamentos',on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
    @property
    def num_funcionarios(self):
        return self.funcionarios.all().count()
