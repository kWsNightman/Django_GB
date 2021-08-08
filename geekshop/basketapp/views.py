from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView
from rest_framework import viewsets, permissions

from adminapp import serializers
from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product


class BasketListView(ListView):
    model = Basket
    template_name = 'basketapp/basket.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user.pk).order_by('product__category')


class AddToBasketView(View):

    def get(self, request, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        basket = Basket.objects.filter(user=request.user, product=product).first()

        if not basket:
            basket = Basket(user=request.user, product=product)

        basket.quantity += 1
        basket.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RemoveFromBasketView(View):

    def get(self, request, **kwargs):
        remove_item = get_object_or_404(Basket, pk=self.kwargs['pk'])
        remove_item.delete()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class BasketEditView(View):

    def get(self, reqest, **kwargs):
        if self.request.is_ajax():
            quantity = int(self.kwargs['quantity'])
            new_basket_item = Basket.objects.get(pk=int(self.kwargs['pk']))

            if quantity > 0:
                new_basket_item.quantity = quantity
                new_basket_item.save()
            else:
                new_basket_item.delete()

            basket = Basket.objects.filter(user=self.request.user.pk).order_by('product__category')
            basket_count = Basket.objects.filter(user=self.request.user)

            context = {
                'basket': basket,
                'basket_count': basket_count
            }

            i = render_to_string('basketapp/includes/inc_main_menu_basket.html', context)
            result = render_to_string('basketapp/includes/inc_basket_list.html', context)

            return JsonResponse({'result': result, 'i': i})
