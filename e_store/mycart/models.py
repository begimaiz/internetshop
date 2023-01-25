from django.contrib.auth.models import User
from django.db import models
from main.models import Product


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    name = models.CharField(default='', max_length=20)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')

    quantity = models.PositiveIntegerField(default=0)

