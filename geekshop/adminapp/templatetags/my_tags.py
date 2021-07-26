from django import template

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'product_images/default.jpg'
    return f'{string}'


register.filter('media_folder_products', media_folder_products)
