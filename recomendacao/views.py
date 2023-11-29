from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.http import JsonResponse
from .models import Historico
from .recomendation import Recomendar
from .recomendation import dividir_conjunto_de_dados
from .recomendation import Carregar_Dataset
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import os
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
    historico_entries = Historico.objects.filter(usuario=request.user).order_by('-data_entrada')
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

def Menu_avancado(request):
    if request.method == 'POST':
        random_state = int(request.POST.get('random_state', 42))  # Valor padrão 42 se não for fornecido
        test_size = float(request.POST.get('test_size', 0.2))  # Valor padrão 0.2 se não for fornecido
        modelo_selecionado = request.POST.get('modelo')


        request.session['random_state'] = random_state
        request.session['test_size'] = test_size


        if modelo_selecionado == 'DecisionTree':
            request.session['train_model'] = '1'
        elif modelo_selecionado == 'GaussianNB':
            request.session['train_model'] = '2'
        elif modelo_selecionado == 'SVC':
            request.session['train_model'] = '3'
        elif modelo_selecionado == 'LogisticRegression':
            request.session['train_model'] = '4'
        elif modelo_selecionado == 'LDA':
            request.session['train_model'] = '5'
        elif modelo_selecionado == 'RF':
            request.session['train_model'] = '6'
        elif modelo_selecionado == None:
            request.session['train_model'] = None

            


        return render(request,'recomendacao.html', {'recomendacao': recomendacao})

    return render(request, 'index.html')  # Exibe o formulário inicial

@csrf_exempt
def recomendacao(request):
    train_model = request.session.get('train_model')
    random_state = request.session.get('random_state', 42)
    test_size = request.session.get('test_size', 0.2)

    DecisionTree = DecisionTreeClassifier()
    Svc = SVC()
    Gaussian = GaussianNB()
    LR = LogisticRegression()
    LDA = LinearDiscriminantAnalysis()
    RandomForest = RandomForestClassifier()
    if request.method == 'POST':
        form = EntradaDadosForm(request.POST)
        if form.is_valid():
            dados_usuario = form.cleaned_data
            if train_model == '1':
                recomendacao = Recomendar(dados_usuario, DecisionTree, random_state, test_size)
            if train_model == '2':
                recomendacao = Recomendar(dados_usuario, Gaussian, random_state, test_size)
            if train_model == '3':
                recomendacao = Recomendar(dados_usuario, Svc, random_state, test_size)
            if  train_model == '4':
                recomendacao = Recomendar(dados_usuario, LR, random_state, test_size)
            if  train_model == '5':
                recomendacao = Recomendar(dados_usuario, LDA, random_state, test_size)
            if train_model == '6':
                recomendacao = Recomendar(dados_usuario, RandomForest, random_state, test_size)
            if train_model == None:
                recomendacao = Recomendar(dados_usuario, DecisionTree, random_state, test_size)
            # Crie uma instância do modelo Historico e salve os dados


            if request.user.is_authenticated:
                historico = Historico(
                usuario=request.user,
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