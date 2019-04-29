from django.db import models


class Cpf(models.Model):
    Numero = models.CharField(max_length=11)
    data_exp = models.DateTimeField(auto_now=False)
   
    def __str__(self):
        return self.Numero


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(Cpf, null=True, blank=True, on_delete=True)
    dt_criacao = models.DateTimeField()

    # Convert object for view
    
    def __str__(self):
        return self.nome


class Telefone(models.Model):
    telefone = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=True)

    def __str__(self):
        return self.telefone + ' - ' + self.descricao


class Produt(models.Model):
    nome = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)
    data = models.DateTimeField()  # Exibe o calendário e horario na view

    # rename a table

    class Meta:
        verbose_name_plural = 'Produtos'

    # Converte object para o nome de eximição na  view
    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    # Converte objeto para o nome de eximição na  view
    def __str__(self):
        return self.nome
