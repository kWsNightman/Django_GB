from .models import Basket


def basket_count(request):
    total_cost = 0
    total_count = 0
    if request.user.is_authenticated:
        basket_counter = Basket.objects.filter(user=request.user)
        if basket_counter:
            b = basket_counter[0].product_quantity_cost
            total_count += b[0]
            total_cost += b[1]
    return {'total_cost': total_cost, 'total_count':total_count}
