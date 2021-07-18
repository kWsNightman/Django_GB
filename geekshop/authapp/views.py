from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from authapp.forms import ShopUserLoginForm, ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser


class UserLoginView(LoginView):
    authentication_form = ShopUserLoginForm
    template_name = 'authapp/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = reverse_lazy('index')
    extra_context = {'title': 'вход', 'operation_name': 'вход в систему'}


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UserRegisterCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': 'регистрация', 'operation_name': 'регистрация'}


class UserEditUpdateView(UpdateView):
    model = ShopUser
    template_name = 'authapp/edit.html'
    form_class = ShopUserEditForm
    success_url = reverse_lazy('auth:edit')
    extra_context = {'title': 'редактирование', 'operation_name': 'редактирование профиля'}

    def get_object(self, **kwargs):
        return self.request.user
