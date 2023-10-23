from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.http import JsonResponse
from .models import Historico
from django.http import HttpResponse
from django.contrib import messages
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
            return redirect('index')
    context = {'form' :form}
    return render(request, 'register.html', context)

def Historico_view(request):
    historico_entries = Historico.objects.filter(usuario=request.user)
    return render(request, 'historico.html', {'historico_entries': historico_entries})


def deletar_historico(request, historico_id):
    historico = Historico.objects.get(id=historico_id)
    if historico.usuario == request.user:
        historico.delete()
    return redirect('historico')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_django(request, user)
            return redirect('index.html')
        else:
            messages.error(request, "Nome de Usuário ou senha incorretas !")
            return redirect('login.html')
        
    return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def recomendacao(request):
    if request.method == 'POST':
        form = EntradaDadosForm(request.POST)
        if form.is_valid():
            dados_usuario = form.cleaned_data
            recomendacao = Recomendar(dados_usuario)
            # Crie uma instância do modelo Historico e salve os dados
            historico = Historico(
                usuario=request.user,  # Substitua isso pelo usuário real (se disponível)
                n=dados_usuario['N'],
                p=dados_usuario['P'],
                k=dados_usuario['K'],
                temperatura=dados_usuario['temperatura'],
                umidade=dados_usuario['umidade'],
                ph=dados_usuario['ph'],
                chuva=dados_usuario['chuva'],
                resposta_ia=recomendacao
            )
            historico.save()
            
            return JsonResponse({'recomendacao': recomendacao})
        return JsonResponse({'error': 'Método não suportado'}, status=405)
    return render(request, 'recomendacao.html')


