from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField('nome',max_length=100)
    dono = models.ForeignKey(User,on_delete=models.PROTECT,related_name='empresa')

    def __str__(self):
        return self.nome