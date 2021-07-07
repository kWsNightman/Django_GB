from .models import Basket


def basket_count(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).values('quantity')
        basket = sum([i['quantity'] for i in basket])
    return {'basket_count': basket}
