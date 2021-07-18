from django.contrib.auth.decorators import login_required
from django.urls import path

import authapp.views
from .views import *

app_name = 'authapp'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('edit/', login_required(UserEditUpdateView.as_view()), name='edit'),

]
