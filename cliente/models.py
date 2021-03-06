from django.db import models


class Cpf(models.Model):
    Numero = models.CharField(max_length=11)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.Numero


# class Grupo(models.Model):
#     nome = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    # cpf = models.OneToOneField(Cpf, null=True, blank=True, on_delete=True)
    cpf = models.CharField(max_length=11)
    # grupo = models.ManyToManyField(Grupo, blank=False)
    foto = models.ImageField(upload_to='cliente/avatar')

    # Convert object for view

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    def to_dirc_Json(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'endereco': self.endereco,
            'salario': self.salario,
            'idade': self.idade,
            'email': self.email,
            'cpf': self.cpf,
        }
        return data


class Telefone(models.Model):
    telefone = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=False)

    def __str__(self):
        return self.descricao
