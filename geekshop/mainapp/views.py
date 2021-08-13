import random

from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import ProductCategory, Product


def get_hot_product():
    product = Product.objects.all()
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
        'links_menu': ProductCategory.objects.all().exclude(is_deleted=True),
    }

    def get_queryset(self):
        if self.kwargs.get('pk') is not None:
            self.paginate_by = 3
            if self.kwargs['pk'] == 0:
                self.extra_context['category'] = {'name': 'все', 'pk': 0}
                return Product.objects.all().filter(is_deleted=False).order_by('price')
            else:
                self.extra_context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
                return Product.objects.filter(is_deleted=False, category__pk=self.kwargs['pk']).order_by('price')

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
        'links_menu': ProductCategory.objects.all().exclude(is_deleted=True),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['same_products'] = get_same_products(self.object_list)
        return context

    def get_queryset(self):
        return Product.objects.get(pk=self.kwargs['pk'])
