from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from rest_framework import viewsets
from adminapp import serializers

from adminapp.forms import CategoryCreateForm, CategoryUpdateForm
from mainapp.models import ProductCategory, Product
from .user import IsAdminUserPassedTestMixin


class ProductCategoryCreateView(IsAdminUserPassedTestMixin, CreateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'adminapp/category/category_create.html'
    success_url = reverse_lazy('admin_staff:categories')
    extra_context = {'title': 'категории/создать'}


class ProductCategoriesListView(IsAdminUserPassedTestMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/category/categories.html'
    extra_context = {'title': 'админка/категории'}
    context_object_name = 'objects'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')
    extra_context = {'title': 'категории/изменение'}
    form_class = CategoryUpdateForm


class ProductCategoryDeleteView(IsAdminUserPassedTestMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category/category_delete.html'
    context_object_name = 'category_to_delete'
    extra_context = {'title': 'категории/удаление'}

    def delete(self, request, *args, **kwargs):
        _object = self.get_object()
        _object.is_deleted = True
        _object.save()

        return HttpResponseRedirect(reverse_lazy('admin_staff:categories'))


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.filter(is_deleted=False)
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            self.serializer_class = serializers.ProductsSerializer
            return Product.objects.filter(category__pk=self.kwargs.get('pk'))
        else:
            return ProductCategory.objects.filter(is_deleted=False)


