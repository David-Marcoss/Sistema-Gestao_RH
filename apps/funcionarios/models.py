from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresa.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField('nome',max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    Empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)

    def __str__(self):
        return self.nome