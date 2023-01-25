from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    MAINS = 'MA'
    SOUPS = 'SO'
    SIDES = 'SI'
    DESSERTS = 'DE'
    SALADS = 'SA'
    DRINKS = 'DR'
    CATEGORY_CHOICES = [
        (MAINS, 'Mains'),
        (SOUPS, 'Soups'),
        (SIDES, 'Sides'),
        (DESSERTS, 'Desserts'),
        (DRINKS, 'Drinks'),
        (SALADS, 'Salads'),
    ]


    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=MAINS,
    )

    description = models.TextField()
    image = models.ImageField(default='', upload_to='static/assets/img/products')
    size = models.IntegerField(default=0)


    rating = models.IntegerField(default=0)
    comments = models.IntegerField()

class Customer(models.Model):
    user = models.OneToOneField(User, default='2', on_delete=models.CASCADE)
    phone_number = models.CharField(default=' ', max_length=20)
    address = models.TextField(default=' ')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # other fields

