from django.shortcuts import render
#import category model
from rango.models import Category

def index(request):
    #query database for list of all categories
    #order categories by likes, descending
    #retrive top 5 only
    #place list in context_dict dictionary
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    #render response and send it back
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

