from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product


def cart_summary(request):
    return render(request, 'store/cart/summary.html')


def cart_add(request):
    cart = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
