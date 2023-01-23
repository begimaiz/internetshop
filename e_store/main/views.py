from django.contrib.auth.models import User
from django.urls import reverse

from .forms import RegisterForm
from .models import Product, Customer
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . import forms


def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')



def shop_single(request):
    return render(request, 'main/shop-single.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'main/shop-single.html', context)


def product_list(request):
    products = Product.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # Show 9 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'main/shop.html', {'products': products})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'username already exists')
                return render(request, 'main/register.html', {'form': form})
            elif Customer.objects.filter(email=email).exists():
                form.add_error('email', 'email already exists')
                return render(request, 'main/register.html', {'form': form})
            elif Customer.objects.filter(username=username).exists():
                form.add_error('username', 'username already exists')
                return render(request, 'main/register.html', {'form': form})
            else:
                new_user = User.objects.create_user(username, email, password)
                new_customer = Customer.objects.create(user=new_user, email=email, username=username)
                return redirect(reverse('index'))
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('main:index')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = forms.LoginForm()
    return render(request, 'main/login.html', {'form': form})

