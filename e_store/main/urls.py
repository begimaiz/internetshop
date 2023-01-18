from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.index, name='index'),
    # path('shop.html', views.shop, name='shop'),
    path('shop-single.html', views.shop_single, name='shop-single'),
    path('login.html', views.login, name='login'),
    path('shop.html', views.product_list, name='product_list'),
    path('shop-single/<int:product_id>/', views.product_detail, name='product_detail'),

]