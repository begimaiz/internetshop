from django.core.checks import messages
from django.db.models import Sum, F
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Cart, CartItem
from main.models import Product
from django.contrib.auth.decorators import login_required
from django import template

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created_cart = Cart.objects.get_or_create(user=request.user)
    quantity = request.POST.get('quantity', 1)
    total_price = product.price * int(quantity)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.quantity += int(quantity)
        cart_item.total_price = cart_item.quantity * product.price
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity, total_price=total_price)
    cart_item.save()

    return redirect(reverse('view_cart'))

@login_required
def remove_from_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product=product)

        if cart_item.quantity >= 2:
            cart_item.quantity -= 1
            cart_item.total_price = cart_item.quantity * product.price
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        # Handle the case where the CartItem is not found
        pass
    return redirect(reverse('view_cart'))

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user.id)


    total =0
    for item in cart_items:
        total += item.total_price
    delivery = 200
    subtotal = total + delivery
    context = {'cart_items': cart_items, 'total':total, 'subtotal':subtotal, 'delivery':delivery}

    return render(request, 'mycart/cart.html', context)

@login_required
def filter_cart_items(request):
    cart_items = CartItem.objects.select_related('product').filter(cart__user=request.user).order_by('product__price')

    total = 0
    for item in cart_items:
        total += item.total_price
    delivery = 200
    subtotal = total + delivery
    context = {'cart_items': cart_items, 'total': total, 'subtotal': subtotal, 'delivery': delivery}

    return render(request, 'mycart/cart.html', context)



register = template.Library()

@register.simple_tag
def cart_total(items):
    total = 0
    for item in items:
        total += item.price * item.quantity
    return total