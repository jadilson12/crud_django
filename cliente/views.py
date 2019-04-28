from django.shortcuts import render
import datetime

def home(request):

    # dicionario vario
    data ={}

    # Propriedade do dicionario adionando now
    data['agora'] = datetime.datetime.now()
    return render(request,'cliente/home.html', data)
