from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField(auto_now_add=True)
