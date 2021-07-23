import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.mail import send_mail
from django.urls import reverse

from geekshop import settings
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar',)

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return data

    @staticmethod
    def send_verify_email(user):
        verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
        title = f'Активация на сайте, пользователя - {user.username}'
        message = f'Для активации вашей учетной {user.email} записи на портале {settings.DOMAIN_NAME} ' \
                  f'перейдите по ссылке \n{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def save(self, commit=True):
        user = super(ShopUserRegisterForm, self).save()

        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        self.send_verify_email(user)
        return user


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')
        return data
