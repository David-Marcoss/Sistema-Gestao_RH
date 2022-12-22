from django.db import models

# Create your models here.

class Hora_extra(models.Model):
    motivo = models.CharField('Motivo',max_length=100)

    def __str__(self):
        return self.motivo