from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from mainapp.models import Product


class OrderItemQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(OrderItemQuerySet, self).delete(*args, **kwargs)


class Order(models.Model):
    objects = OrderItemQuerySet.as_manager()

    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEED = 'PCD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDERS_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    update = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=ORDERS_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    @cached_property
    def get_items_cachet(self):
        return self.orderitems.select_related()

    def get_summary(self):
        items = self.get_items_cachet
        return {
            'total_coast': sum(list(map(lambda x: x.quantity * x.product.price, items))),
            'total_quantity': sum(list(map(lambda x: x.quantity, items)))
        }

    def get_total_quantity(self):
        items = self.get_items_cachet
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.get_items_cachet
        return len(items)

    def get_total_cost(self):
        items = self.get_items_cachet
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(OrderItem, self).delete()
