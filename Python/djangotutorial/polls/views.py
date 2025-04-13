from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, estás en la página de encuestas.")

def home(request):
    return HttpResponse("Bienvenido a la página principal de mi sitio Django.")