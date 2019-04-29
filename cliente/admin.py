from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'endereco', 'email', 'idade', 'cpf')


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'descricao', 'cliente')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produt)
admin.site.register(Categoria)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Cpf)
admin.site.register(Grupo)
