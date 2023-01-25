from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from main.models import Product



@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, customer=request.user)
    context = {'mycart': cart}
    return render(request, 'mycart/cart.html', context)


def create_cart_item(cart, product, quantity):
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem(product=product, cart=cart)
        cart_item.quantity = quantity
        cart_item.name = product.name

    cart_item = CartItem(product=product, cart=cart)
    cart_item.quantity = quantity
    cart_item.name = product.name

    print('--',cart_item)
    return cart_item

@login_required
def cart_add(request, product_id):
    quantity = 1
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    try:
        cart = Cart.objects.get(customer=user)
        item = create_cart_item(cart, product, quantity)
        print('cart exists and added item', item)

        context = {'mycart': cart}
        return render(request, 'mycart/cart.html', context)


    except Cart.DoesNotExist:
        cart, created = Cart.objects.get_or_create(customer=user)
        create_cart_item(cart, product, quantity)
        context = {'mycart': cart}
        return render(request, 'mycart/cart.html', context)

