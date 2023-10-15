from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from .recomendation import *

class EntradaDadosForm(forms.Form):
    N = forms.FloatField(label='Nitrogênio')
    P = forms.FloatField(label='Fósforo')
    K = forms.FloatField(label='Potássio')
    temperatura = forms.FloatField(label='Temperatura')
    umidade = forms.FloatField(label='Umidade')
    ph = forms.FloatField(label='Ph')
    chuva = forms.FloatField(label='Chuva')


def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
             
            login_django(request, user)
            return render(request, 'index.html')
        else:
            form = UserCreationForm()
    context = {'form' :form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            print('sei la')
    else: 
        return render(request, 'login.html')

@csrf_exempt
def recomendacao(request):
    if request.method == 'POST':
        form = EntradaDadosForm(request.POST)
        if form.is_valid():
            dados_usuario = form.cleaned_data
            recomendacao = Recomendar(dados_usuario)
            return JsonResponse({'recomendacao': recomendacao})
        return JsonResponse({'error': 'Método não suportado'}, status=405)
    return render(request, 'recomendacao.html')


