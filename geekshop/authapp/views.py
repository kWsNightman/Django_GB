from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from authapp.forms import ShopUserLoginForm, ShopUserEditForm, ShopUserRegisterForm, ShopUserProfileEditForm
from authapp.models import ShopUser


class UserVerifyView(View):
    def get(self, request, **kwargs):
        try:
            user = ShopUser.objects.get(email=self.kwargs['email'])
            if user.activation_key == self.kwargs['activation_key'] and not user.is_activation_expired():
                user.is_active = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, 'authapp/verification.html')
            else:
                return render(request, 'authapp/verification.html')
        except Exception as err:
            print(err)


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


class UserEditUpdateView(UpdateView):  # Возможно лучше делать через наследование класса View
    model = ShopUser
    template_name = 'authapp/edit.html'
    form_class = ShopUserEditForm
    success_url = reverse_lazy('auth:edit')
    extra_context = {'title': 'редактирование', 'operation_name': 'редактирование профиля'}

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = {'form_profile': ShopUserProfileEditForm(instance=self.get_object().shopuserprofile)}
        return super(UserEditUpdateView, self).get_context_data(**context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        super(UserEditUpdateView, self).post(request)
        form = self.get_form()
        form_profile = ShopUserProfileEditForm(request.POST, instance=self.get_object().shopuserprofile)
        # Тут скорее всего есть ошибка оно не так должно делаться наверное но пока что работает
        if form.is_valid() and form_profile.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
