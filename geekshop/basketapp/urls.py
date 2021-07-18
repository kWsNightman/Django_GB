from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'basket'

urlpatterns = [
    path('', login_required(BasketListView.as_view()), name='view'),
    path('add/<int:pk>/', login_required(AddToBasketView.as_view()), name='add'),
    path('remove/<int:pk>/', login_required(RemoveFromBasketView.as_view()), name='remove'),
    path('edit/<int:pk>/<int:quantity>/', login_required(BasketEditView.as_view()), name='edit'),
]
