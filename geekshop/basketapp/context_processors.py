from .models import Basket


# Я контекстный процессор выполнял раннее для корзины
def basket_count(request):
    basket_counter = []
    if request.user.is_authenticated:
        basket_counter = Basket.objects.filter(user=request.user)
    return {'basket_count': basket_counter}
