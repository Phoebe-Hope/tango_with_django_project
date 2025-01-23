from django.shortcuts import render
#import category model
from rango.models import Category
from rango.models import Page

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

def show_category(request, category_name_slug):
    #create context dictionarywhich we can pass to the template rendering engine
    context_dict = {}

    try:
        #use .get() to find category name slug with given name, DoesNotExist exception raised if not
        category = Category.objects.get(slug=category_name_slug)

        #get all associated pages, filter() will return list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        #adds our results list to the template context under name pages
        context_dict['pages'] = pages
        #add category object from the database to the context dictionary
        #use this template to verify that the category exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        #here if category isn't found
        #dont need to do anything - template will display no category message
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html',  context=context_dict)

