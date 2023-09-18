from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def recomendacao(request):
    return render(request, 'recomendacao.html')

def jsonviewer(request):
    return render(request, 'jsonview.html')


def funcao_de_visualizacao(request):
    if request.method == 'POST':
        # Obter os dados enviados pelo frontend (no formato JSON)
        data = json.loads(request.body)

        # Agora, você pode acessar os dados individualmente, por exemplo:
        n = data.get('n')
        p = data.get('p')
        k = data.get('k')
        temperatura = data.get('temperatura')
        umidade = data.get('umidade')
        ph = data.get('ph')
        

        # Faça o processamento necessário com esses dados, como usar seu modelo de Machine Learning.

        # Retorne uma resposta (por exemplo, uma recomendação) para o frontend
        resposta = {'recomendacao': 'Recomendação aqui'}
        return HttpResponse(json.dumps(resposta), content_type='application/json')
    
    return HttpResponse(status=400)  # Responda com erro se não for uma solicitação POST válida

# Create your views here.
