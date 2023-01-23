from django.contrib.auth.models import AbstractUser, User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comments = models.IntegerField()
    brand = models.CharField(max_length=255)
    description = models.TextField()
    available_colors = models.CharField(max_length=255)
    specification = models.TextField()
    image = models.ImageField(default='', upload_to='static/assets/img/products')

class Customer(models.Model):
    user = models.OneToOneField(User, default='2', on_delete=models.CASCADE)
    phone_number = models.CharField(default=' ', max_length=20)
    address = models.TextField(default=' ')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # other fields
