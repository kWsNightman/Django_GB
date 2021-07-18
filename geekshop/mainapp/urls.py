from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductsListView.as_view(), name='category'),
    # path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
]
