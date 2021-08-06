from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from rest_framework import viewsets, permissions

from adminapp import serializers
from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser


class IsAdminUserPassedTestMixin(UserPassesTestMixin):
    login_url = '/auth/login/'
    redirect_field_name = 'next'

    def test_func(self):
        return self.request.user.is_superuser


class UserCreateView(IsAdminUserPassedTestMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user/user_create.html'
    extra_context = {'title': 'пользователи/создать'}
    form_class = ShopUserRegisterForm
    success_url = '/admin_staff/users/read/'


class UsersListView(IsAdminUserPassedTestMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/user/users.html'
    context_object_name = 'objects'
    extra_context = {'title': 'админка/пользователи'}
    paginate_by = 3
    ordering = ('is_deleted', '-is_active', '-is_superuser', '-is_staff', 'username')


class UserUpdateView(IsAdminUserPassedTestMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user/user_update.html'
    form_class = ShopUserAdminEditForm
    success_url = reverse_lazy('admin_staff:users')
    extra_context = {'title': 'пользователи/редактировать'}


class UserDeleteView(IsAdminUserPassedTestMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')
    extra_context = {'title': 'пользователи/удаление'}
    context_object_name = 'user_to_delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ShopUserViewSet(viewsets.ModelViewSet):
    queryset = ShopUser.objects.all()
    serializer_class = serializers.ShopUserSerializer

    def list(self, request, *args, **kwargs):
        print(request)
        return super(ShopUserViewSet, self).list(request,*args,**kwargs)