from django.db import models


class Empresa(models.Model):
    nome = models.CharField('nome',max_length=100)

    def __str__(self):
        return self.nome