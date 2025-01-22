from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("<h1>Rango says here is the about page.</h1><p><a href='/rango/'>Index</a></p>")