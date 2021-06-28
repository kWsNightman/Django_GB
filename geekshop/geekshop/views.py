from django.shortcuts import render

from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:3]
    context = {
        'title': 'магазин',
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'contact.html', context=context)
