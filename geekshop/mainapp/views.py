from django.shortcuts import render
from .models import ProductCategory


# Create your views here.
def products(request, pk=None):
    links_menu = [{'name': 'все'}]
    links_menu += ProductCategory.objects.all()
    context = {
        'title': 'каталог',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context=context)
