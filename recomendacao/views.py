from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def recomendacao(request):
    return render(request, 'recomendacao.html')

# Create your views here.
