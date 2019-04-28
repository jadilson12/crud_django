from django.shortcuts import render
import datetime

def home(request):

    # dicionario vario
    data ={}

    # Lista de produtos
    data['diversos'] = ['Carro', 'motos','avião', 'animais']

    # Propriedade do dicionario adionando now
    data['agora'] = datetime.datetime.now()
    return render(request,'cliente/home.html', data)
