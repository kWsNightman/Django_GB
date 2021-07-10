from .models import Basket


def basket_count(request):
    basket_count = []
    if request.user.is_authenticated:
        basket_count = Basket.objects.filter(user=request.user)
    return {'basket_count': basket_count}
