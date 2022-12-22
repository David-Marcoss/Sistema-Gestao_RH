from django.db import models

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField('Descricao',max_length=80)


    def __str__(self):
        return self.descricao