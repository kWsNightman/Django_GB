import random

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import ProductCategory, Product


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_deleted=False)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_deleted=False)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_deleted=False,category__is_deleted=False).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_deleted=False,category__is_deleted=False).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_ordered_by_price():
    if settings.LOW_CACHE:
        key = 'products_ordered_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_deleted=False,category__is_deleted=False).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_deleted=False,category__is_deleted=False).order_by('price')


def get_products_in_category_ordered_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_ordered_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_deleted=False,category__is_deleted=False).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_deleted=False,category__is_deleted=False).order_by('price')


def get_hot_product():
    product = get_products()
    return random.choice(product)


def get_same_products(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
    return same_products


class ProductsListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'

    context_object_name = 'products'
    ordering = 'price'
    extra_context = {
        'title': 'каталог',
        'links_menu': get_links_menu(),
    }

    def get_queryset(self):
        if self.kwargs.get('pk') is not None:
            self.paginate_by = 3
            if self.kwargs['pk'] == 0:
                self.extra_context['category'] = {'name': 'все', 'pk': 0}
                return get_products_ordered_by_price()
            else:
                self.extra_context['category'] = get_category(pk=self.kwargs['pk'])
                return get_products_in_category_ordered_by_price(pk=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        if self.kwargs.get('pk') is None:
            hot_product = get_hot_product()
            context['hot_product'] = hot_product
            context['same_products'] = get_same_products(hot_product)

        return context


class ProductListView(ListView):
    model = Product
    template_name = 'mainapp/product.html'
    context_object_name = 'product'
    extra_context = {
        'title': 'продукты',
        'links_menu': get_links_menu(),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['same_products'] = get_same_products(self.object_list)
        return context

    def get_queryset(self):
        return get_product(pk=self.kwargs['pk'])
