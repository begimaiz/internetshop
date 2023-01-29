from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('login/', views.login_view, name='login'),

    path('view-cart', views.view_cart, name='view_cart'),
    path('add-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:product_id>/', views.remove_from_cart, name ='remove_from_cart'),
    path('filter-cart-items', views.filter_cart_items, name ='filter_cart_items'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('order/<str:subtotal>', views.order, name='order')

]