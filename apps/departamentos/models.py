from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField('nome',max_length=100)

    def __str__(self):
        return self.nome