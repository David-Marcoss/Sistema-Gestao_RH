from django.db import models

# Create your models here.

class Teste_Db_Antigo(models.Model):
    texto = models.TextField(verbose_name='texto')

    def __str__(self):
        return self.texto
    

class registro_funcionarios(models.Model):
    nome = models.CharField(max_length=100,verbose_name='nome')
    idade =  models.IntegerField(verbose_name='idade')
    salario = models.FloatField(verbose_name=idade)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'registro_funcionarios'