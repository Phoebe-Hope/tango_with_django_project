#population script for rango

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    #First we create lists of dictionaries containing the pages we want to add into each category
    #Then create a dictionary of dictionaries fr our categories
    #This might seem a little bit confusing, but it allows us to iterate
    #through each data structure, and add the data to our models

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
          'url':'http://www.korokithakis.net/tutorials/python/'},
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
          'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
          'url':'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title':'Bottle',
          'url':'http://bottlepy.org/docs/dev/'},
         {'title':'Flask',
          'url':'http://flask.pocoo.org'}
    ]

    cats = {'Python': {'pages': python_pages},
             'Django': {'pages': django_pages},
             'Other Frameworks': {'pages': other_pages} }

    #iterates through cats dictionary, then adds each category and then adds all associated pages for that category
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    #print