from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField(auto_now_add=True)

class Produto(models.Model):
    nome = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacao = models.TextField()
    dt_criacao = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField(auto_now_add=True)