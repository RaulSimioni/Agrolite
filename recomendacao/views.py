from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def recomendacao(request):
    return render(request, 'recomendacao.html')


