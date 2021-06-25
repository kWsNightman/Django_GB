from django.shortcuts import render


def index(request):
    context = {
        'title': 'магазин'
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'contact.html', context=context)
