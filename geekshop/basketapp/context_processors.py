from .models import Basket


def basket_count(request):
    basket_counter = []
    total_cost = 0
    total_count = 0
    if request.user.is_authenticated:
        basket_counter = Basket.objects.filter(user=request.user)
        for i in basket_counter:
            b = i.product_quantity_cost
            total_count += b[0]
            total_cost += b[1]
    return {'total_cost': total_cost, 'total_count':total_count}
