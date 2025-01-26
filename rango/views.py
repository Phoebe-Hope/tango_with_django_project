from django.shortcuts import render
#import category model
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm, PageForm
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    #query database for list of all categories
    #order categories by likes, descending
    #retrive top 5 only
    #place list in context_dict dictionary
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy,  creamy, cookie, candy,  cupcake! '
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    #render response and send it back
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    #create context dictionary which we can pass to the template rendering engine
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

def add_category(request):
    form = CategoryForm()

    #A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #Have we been provided with a valid form?
        if form.is_valid():
            #save new category to the database
            form.save(commit=True)
            return redirect('/rango/')

        else:
            print(form.errors)

        #will handle the bad form, new form, or no form supplied cases
        #render the form with error messages (if any)
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    #can't add a page to a category that doesn't exist
    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category',
                                        kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

