from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Product
from django.core.paginator import Paginator


def main(request):
    return render(request, 'main/index.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def login(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form.LoginForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('main/login.html')
    return render(request, 'main/login.html')

def contact(request):
    return render(request, 'main/contact.html')


def shop(request):
    return render(request, 'main/shop.html')


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