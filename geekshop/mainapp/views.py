import random

from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def get_hot_product():
    product = Product.objects.all()
    return random.choice(product)


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    return same_products


def products(request, pk=None):
    links_menu = ProductCategory.objects.all().exclude(is_deleted=True)
    products = None
    category = None
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

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
        'hot_product': hot_product,

    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукты'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all().exclude(is_deleted=True),
        'product': get_object_or_404(Product, pk=pk),

    }
    return render(request, 'mainapp/product.html', context)
