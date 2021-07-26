from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from authapp.forms import ShopUserLoginForm, ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser


# def send_verify_email(user):
#     verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
#     title = f'Активация на сайте, пользователя - {user.username}'
#     message = f'Для активации вашей учетной {user.email} записи на портале {settings.DOMAIN_NAME}' \
#               f'перейдите по ссылке \n{settings.DOMAIN_NAME}{verify_link}'
#     return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


class UserVerifyView(View):
    def get(self, request, **kwargs):
        try:
            user = ShopUser.objects.get(email=self.kwargs['email'])
            if user.activation_key == self.kwargs['activation_key'] and not user.is_activation_expired():
                user.is_active = True
                user.save()
                auth.login(request, user)
                return render(request, 'authapp/verification.html')
            else:
                return render(request, 'authapp/verification.html')
        except Exception as err:
            print('Error')

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

    # def form_valid(self, form):
    #     self.object = form.save()
    #     if send_verify_email(self.object):
    #         print('Сообщение отправлено')
    #     else:
    #         print('сообщение не отправлено')
    #     return super(UserRegisterCreateView, self).form_valid(form)


class UserEditUpdateView(UpdateView):
    model = ShopUser
    template_name = 'authapp/edit.html'
    form_class = ShopUserEditForm
    success_url = reverse_lazy('auth:edit')
    extra_context = {'title': 'редактирование', 'operation_name': 'редактирование профиля'}

    def get_object(self, **kwargs):
        return self.request.user
