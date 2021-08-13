from django.db import models

from geekshop import settings
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0, )
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True, )
    is_deleted = models.BooleanField(default=False)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def product_quantity_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return [_total_quantity, _total_cost]

    # @staticmethod
    # def get_item(pk):
    #     return Basket.objects.filter(pk=pk).first()

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f'Корзина {self.user}: {self.product}'
