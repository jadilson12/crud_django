from django.shortcuts import render, redirect
from .models import *
from .form import *
import datetime


def home(request):
    # dicionario vario
    data = {}

    # Lista de produtos
    data['diversos'] = ['Carro', 'motos', 'avião', 'animais']

    # Propriedade do dicionario adionando now
    data['agora'] = datetime.datetime.now()
    return render(request, 'cliente/home.html', data)


def clientes(request):
    data = {'clientes': Cliente.objects.all()}
    return render(request, 'cliente/lista.html', data)


def novo_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)
    # validar
    if form.is_valid():
        form.save()
        return redirect('ListaClientes')
    data['form'] = form
    return render(request, 'cliente/novoCliente.html', data)


def update_cliente(request, pk):
    data = {}
    clientes = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=clientes)
  
    # validar
    if form.is_valid():
        form.save()
        return redirect('ListaClientes')
    data['form'] = form
    return render(request, 'cliente/novoCliente.html', data)
