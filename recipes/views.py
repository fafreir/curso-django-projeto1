from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', status=201)


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse("Sobre")
