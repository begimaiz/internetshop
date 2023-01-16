from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.


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