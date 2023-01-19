# Create your views here.

from django.http import HttpResponse

def saludo(request):
      return HttpResponse("Esta la primera página del blog")

def despedida(request):
      return HttpResponse("Esta es la página de despedida")