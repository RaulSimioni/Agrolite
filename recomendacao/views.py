from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

def login(request):
    return render(request, "profile.html")

def logout(request):
    pass

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faça o login do usuário automaticamente após o registro
            login(request, user)
            return redirect("{% url index %}")  # Redirecione para a página de sucesso de registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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


