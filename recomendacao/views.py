from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .recomendation import *

class EntradaDadosForm(forms.Form):
    N = forms.FloatField(label='Nitrogênio')
    P = forms.FloatField(label='Fósforo')
    K = forms.FloatField(label='Potássio')
    Temperatura = forms.FloatField(label='Temperatura')
    Umidade = forms.FloatField(label='Umidade')
    Ph = forms.FloatField(label='Ph')
    Chuva = forms.FloatField(label='Chuva')

def index(request):
    return render(request, 'index.html')

def recomendacao(request):
    if request.method == 'POST':
        form = EntradaDadosForm(request.POST)
        if form.is_valid():
            dados_usuario = form.cleaned_data  # Obtém os dados do formulário
            recomendacao = Recomendar(dados_usuario)
            return JsonResponse({'recomendacao': recomendacao})
        return JsonResponse({'error': 'Método não suportado'}, status=405)
    return render(request, 'recomendacao.html')


