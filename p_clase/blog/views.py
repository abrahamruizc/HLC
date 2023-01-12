from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def saludo(request):
      return HTTPResponse("Esta la primera página del blog")

def despedida(request):
      return HTTPResponse("Esta es la página de despedida")