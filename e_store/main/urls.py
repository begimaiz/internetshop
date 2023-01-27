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

    path('shop/<str:category>/', views.filter_products, name='filter_products'),
    path('filter-sort/', views.filter_sort, name='filter_sort'),
]
