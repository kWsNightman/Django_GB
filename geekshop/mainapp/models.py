from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True, )
    description = models.TextField(verbose_name='описание', blank=True, )
    is_deleted = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name='категория', on_delete=models.CASCADE,)
    name = models.CharField(verbose_name='имя продукта', max_length=128,)
    image = models.ImageField(upload_to='product_images', verbose_name='изображение', blank=True,)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=256, blank=True,)
    description = models.TextField(verbose_name='описание продукта', blank=True,)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0,)
    quantity = models.PositiveIntegerField(verbose_name='количество товара на складе', default=0,)
    is_deleted = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
