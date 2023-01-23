from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),

    path('shop/', views.product_list, name='product_list'),
    path('shop-single/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('login.html', views.login, name='login'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]