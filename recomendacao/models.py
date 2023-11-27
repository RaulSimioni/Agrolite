from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class  Historico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField(auto_now_add=True)
    n = models.FloatField()
    p = models.FloatField()
    k = models.FloatField()
    temperatura = models.FloatField()
    umidade = models.FloatField()
    ph = models.FloatField()
    chuva = models.FloatField()
    resposta_ia = models.CharField(max_length=255)


