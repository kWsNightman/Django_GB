from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from adminapp.forms import ProductEditForm
from mainapp.models import ProductCategory, Product
from .user import IsAdminUserPassedTestMixin


class ProductCreateView(IsAdminUserPassedTestMixin, CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/products/product_create.html'
    extra_context = {'title': "продукты/создание"}

    def get_initial(self):
        self.initial = {'category': get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))}
        return self.initial

    def get_success_url(self):
        return reverse('admin_staff:products', args=[self.request.POST.get('category')])


class ProductsListView(IsAdminUserPassedTestMixin, ListView):
    model = Product
    template_name = 'adminapp/products/products.html'
    context_object_name = 'objects'
    extra_context = {'title': 'админка/продукт'}
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk')).order_by('is_deleted', 'name')


class ProductUpdateView(IsAdminUserPassedTestMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/products/product_update.html'
    extra_context = {'title': "продукты/редактирование"}

    def get_initial(self):
        _object = self.get_object()
        self.initial = {'category': _object.category}
        return self.initial

    def get_success_url(self):
        return reverse('admin_staff:products', args=[self.request.POST.get('category')])


class ProductDeleteView(IsAdminUserPassedTestMixin, DeleteView):
    model = Product
    template_name = 'adminapp/products/product_delete.html'
    extra_context = {'title': 'продукт/удаление'}
    context_object_name = 'product_to_delete'

    def delete(self, request, *args, **kwargs):
        _object = self.get_object()
        _object.is_deleted = True
        _object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        _object = self.get_object()
        return reverse('admin_staff:products', args=[_object.category.pk])


class ProductReadListView(IsAdminUserPassedTestMixin, ListView):
    model = Product
    template_name = 'adminapp/products/product_read.html'
    context_object_name = 'product'
    extra_context = {'title': 'продукты/подробнее'}

    def get_queryset(self):
        return Product.objects.get(pk=self.kwargs.get('pk'))
