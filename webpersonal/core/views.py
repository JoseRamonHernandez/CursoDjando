from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")