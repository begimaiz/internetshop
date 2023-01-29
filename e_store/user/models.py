from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from main.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f"Cart for {self.user.username}"

    def cart_exists(cls, user):
        return cls.objects.filter(user=user).exists()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(30)])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_completed = models.BooleanField(default=False)

    billing_address = models.TextField()
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=20)
    payment_data = models.TextField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'Order #{self.id}'