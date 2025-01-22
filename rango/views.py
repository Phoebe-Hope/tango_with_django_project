from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Rango says hey there partner!</h1><p><a href='/rango/about'>About</a></p>")

def about(request):
    return HttpResponse("<h1>Rango says here is the about page.</h1><p><a href='/rango/'>Index</a></p>")