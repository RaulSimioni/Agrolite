from django.db import models
from django.contrib.auth.models import User

class Historico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    entrada_usuario = models.JSONField()
    resposta_ia = models.CharField(max_length=255)
