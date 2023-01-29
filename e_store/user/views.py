from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import  AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Cart, CartItem, Order
from main.models import Product
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm

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
    total = 0
    for item in cart_items:
        total += item.total_price
    delivery = 200
    subtotal = total + delivery
    context = {'cart_items': cart_items, 'total':str(total), 'subtotal':str(subtotal), 'delivery':str(delivery)}

    return render(request, 'user/cart.html', context)

@login_required
def filter_cart_items(request):
    cart_items = CartItem.objects.select_related('product').filter(cart__user=request.user).order_by('product__price')
    total = 0
    for item in cart_items:
        total += item.total_price
    delivery = 200
    subtotal = total + delivery
    context = {'cart_items': cart_items,'total':str(total), 'subtotal':str(subtotal), 'delivery':str(delivery)}

    return render(request, 'user/cart.html', context)

def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {
        'order': order
    }
    return render(request, 'user/checkout.html', context)


def user(request):
    orders = Order.objects.filter(user=request.user)
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'user/user.html', {'orders':orders, 'cart':cart})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def order(request, subtotal):
    # Retrieve the cart for the current user
    cart = Cart.objects.filter(user=request.user).first()
    subtotal = float(subtotal)
    # Create a new order using the information from the cart
    order = Order.objects.create(user=request.user, total_price=subtotal)

    # Clear the cart
    cart_items = CartItem.objects.filter(cart__user=request.user)
    for item in cart_items:
        item.delete()
    context = {
        'order': order
    }

    return render(request, 'user/checkout.html', context)