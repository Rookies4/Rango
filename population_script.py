import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views': 30}, 
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 56}, 
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views': 90}, 
        {'title': 'Python Tutorial - W3Schools',
        'url':'https://www.w3schools.com/python/',
        'views':22}]


    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 102},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 190},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 234}
    ]


    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 89},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 78}
    ]
    javascript_pages = [
        {'title':'javaScript Tutorial - W3Schools',
         'url':'https://www.w3schools.com/js/',
         'views': 78},
        {'title':'JavaScript Core Language',
         'url':'https://www.pluralsight.com/paths/javascript-core-language',
         'views': 56}
    ]

    perl_pages = [
        {'title':'The Perl Programming Language',
         'url':'https://www.perl.org/',
         'views': 33},
        {'title':"Beginner's Introduction to Perl",
         'url':'https://www.perl.com/pub/2000/10/begperl1.html/',
         'views': 19},
        {'title':"Comprehensive Perl Archive Network",
         'url':'https://www.cpan.org/',
         'views': 23}
    ]
    java_pages = [
        {'title': 'Codecademy Learn Java',
        'url':'https://www.codecademy.com/learn/learn-java',
        'views': 106}, 
        {'title':'The Java™ Tutorials - Oracle Help Center',
        'url':'https://docs.oracle.com/javase/tutorial/',
        'views': 78}, 
        {'title':'Java Tutorial - W3Schools',
        'url':'https://www.w3schools.com/java/',
        'views': 90}, 
        {'title': 'Java Tutorial for Beginners: Learn Core Java Programming',
        'url':'https://www.guru99.com/java-tutorial.html',
        'views':44}
    ]
    prolog_pages = [
        {'title': 'Prolog Tutorial - Tutorialspoint',
        'url':'https://www.tutorialspoint.com/prolog/index.htm',
        'views': 54}, 
        {'title':'Learn Prolog Now!',
        'url':'http://www.let.rug.nl/bos/lpn//',
        'views': 78}, 
        {'title':'Getting started with Prolog Language - RIP Tutorial',
        'url':'https://riptutorial.com/prolog',
        'views': 90}, 
        {'title': 'JProlog Tutorial - javatpoint',
        'url':'https://www.javatpoint.com/prolog',
        'views':44}
    ]
    php_pages = [
        {'title': 'PHP Tutorial - W3Schools',
        'url':'hhttps://www.w3schools.com/php/',
        'views': 97}, 
        {'title':'PHP: The Right Way',
        'url':'https://phptherightway.com/',
        'views': 73}, 
        {'title':'PHP Tutorial - Tutorialspoint',
        'url':'https://www.tutorialspoint.com/php/index.htm',
        'views': 92}, 
        {'title': 'PHP Tutorial for Beginners: Learn in 7 Days - Guru99',
        'url':'hhttps://www.guru99.com/php-tutorials.html',
        'views':36}
    ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            'Javascript': {'pages': javascript_pages, 'views': 16, 'likes': 7},
            'perl': {'pages': perl_pages, 'views': 30, 'likes': 12},
            'java': {'pages': java_pages, 'views': 170, 'likes': 89},
            'prolog': {'pages': prolog_pages, 'views': 22, 'likes': 17},
            'php': {'pages': php_pages, 'views': 34, 'likes': 23},
            }

    
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views = p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'-{c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
