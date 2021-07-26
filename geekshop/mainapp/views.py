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


#
# def products(request, pk=None, page=1):
#     links_menu = ProductCategory.objects.all().exclude(is_deleted=True)
#     products_paginator = None
#     category = None
#     hot_product = None
#     same_products = None
#
#     if pk is not None:
#         if pk == 0:
#             products = Product.objects.all().filter(is_deleted=False).order_by('price')
#             category = {'name': 'все', 'pk': 0}
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.objects.filter(is_deleted=False, category__pk=pk).order_by('price')
#
#         paginator = Paginator(products, 3)
#
#         try:
#             products_paginator = paginator.page(page)
#         except PageNotAnInteger:
#             products_paginator = paginator.page(1)
#         except EmptyPage:
#             products_paginator = paginator.page(paginator.num_pages)
#     else:
#         hot_product = get_hot_product()
#         same_products = get_same_products(hot_product)
#
#     context = {
#         'title': 'каталог',
#         'links_menu': links_menu,
#         'products': products_paginator,
#         'category': category,
#         'same_products': same_products,
#         'hot_product': hot_product,
#     }
#     return render(request, 'mainapp/products.html', context=context)

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
        print(self.object_list)
        context['same_products'] = get_same_products(Product.objects.get(pk=self.kwargs['pk']))
        return context

    def get_queryset(self):
        return Product.objects.get(pk=self.kwargs['pk'])
