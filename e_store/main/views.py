from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from .models import Product, Customer
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from .forms import ContactForm
from . import forms
from mycart import views


def index(request):
    products = Product.objects.order_by('name')

    return render(request, 'main/index.html', {'products': products})


def main(request):
    products = Product.objects.order_by('name')
    return render(request, 'main/index.html', {'products': products})

def about(request):
    return render(request, 'main/about.html')


def shop_single(request):
    return render(request, 'main/shop-single.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'main/shop-single.html', context)


def product_list(request):
    products = Product.objects.order_by('name')
    paginator = Paginator(products, 6)  # Show 6 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'main/shop.html', {'products': products})


def filter_products(request, category):
    products = Product.objects.filter(category=category).order_by('name')
    paginator = Paginator(products, 6) # Show 6 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'main/shop.html', {'products': products})


def filter_objects(sort, category):
    if category =='AL':
        return Product.objects.order_by(sort)
    else:
        return Product.objects.filter(category=category).order_by(sort)


def filter_sort(request):
    # print('called filter_sort')
    sort = request.GET.get('sort_value')
    category = request.GET.get('category')
    if category == '':
        category = 'AL'
    print(sort, category)
    if sort == 'name_asc':
        products = filter_objects('name', category)
    elif sort == 'name_desc':
        products = filter_objects('-name', category)
    elif sort == 'price_asc':
        products = filter_objects('price', category)
    elif sort == 'price_desc':
        products = filter_objects('-price', category)
    elif sort == 'rating_asc':
        products = filter_objects('rating', category)
    elif sort == 'rating_desc':
        products = filter_objects('-rating', category)
    else:
        products = Product.objects.filter(category=category)

    paginator = Paginator(products, 6)  # Show 6 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    # for i in products:
    #     print(i.name)
    return render(request, 'main/shop.html', {'products': products})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "From contact form"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            email_f = settings.EMAIL_HOST_USER
            email_t = 'beka.catering.services@gmail.com'

            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          email_f,
                          [email_t])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("index")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})