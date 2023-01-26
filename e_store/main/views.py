from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, BadHeaderError, send_mail
from django.http import HttpResponse
from django.urls import reverse

from .forms import RegisterForm
from .models import Product, Customer
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from .forms import ContactForm
from . import forms
from mycart import views



def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
#
# def contact(request):
#     return render(request, 'main/contact.html')
#


def shop_single(request):
    return render(request, 'main/shop-single.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'main/shop-single.html', context)


def product_list(request):
    products = Product.objects.all()
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
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = forms.LoginForm()
    return render(request, 'main/login.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # try:
        #     email = EmailMessage(
        #         subject,
        #         message,
        #         'Your Name <from_email@example.com>',
        #         ['to_email@example.com'],
        #         ['bcc_email@example.com'],
        #         reply_to=[email],
        #         )
        #     email.send()
        #     return redirect('success')
        # except:
        #     return redirect('fail')
        #
        send_mail(
            subject,
            message,
            email,
            ['zulpukarovabegimai@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'contact.html')


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

