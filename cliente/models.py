from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField()

    # Converte objeto para o nome de eximição na  view
    def __str__(self):
        return self.nome

class Produt(models.Model):
    nome = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)
    data = models.DateTimeField() # Exibe o calendário e horario na view

    # renomear a tabela
    class Meta:
        verbose_name_plural = 'Produtos'

    # Converte objeto para o nome de eximição na  view
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    # Converte objeto para o nome de eximição na  view
    def __str__(self):
        return self.nome