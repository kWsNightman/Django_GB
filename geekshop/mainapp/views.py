from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


# Create your views here.
def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    products = None
    category = None
    same_products = Product.objects.all()[1:4]

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

    context = {
        'title': 'каталог',
        'links_menu': links_menu,
        'products': products,
        'category': category,
        'same_products': same_products,

    }
    return render(request, 'mainapp/products.html', context=context)
