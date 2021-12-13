from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'главная'

    links_menu = [
        {'href': 'index/', 'name': 'домой'},
        {'href': 'products/', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'geekshop/contacts.html', context=context)

