from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'endereco', 'email', 'idade', 'cpf')
    list_filter = ['grupo']
    search_fields = ['idade','nome', 'id']


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'descricao', 'cliente')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Cpf)
admin.site.register(Grupo)
