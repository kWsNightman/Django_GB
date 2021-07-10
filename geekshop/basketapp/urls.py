from django.urls import path
from .views import basket_add, basket_remove, basket, basket_edit

app_name = 'basket'

urlpatterns = [
    path('', basket, name='view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket_edit, name='edit'),
]
