from django.urls import path
from . import views



urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('view-cart', views.view_cart, name='view_cart'),
    path('add-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:product_id>/', views.remove_from_cart, name ='remove_from_cart'),
    # path('clear/', ClearCartView.as_view(), name='clear_cart'),
    path('filter-cart-items', views.filter_cart_items, name ='filter_cart_items'),
]



