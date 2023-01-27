from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):


    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # -------CATEGORY-------->
    ALL = 'AL'
    MAINS = 'MA'
    SOUPS = 'SO'
    SIDES = 'SI'
    DESSERTS = 'DE'
    SALADS = 'SA'
    DRINKS = 'DR'
    CATEGORY_CHOICES = [
        (ALL, 'All'),
        (MAINS, 'Mains'),
        (SOUPS, 'Soups'),
        (SIDES, 'Sides'),
        (DESSERTS, 'Desserts'),
        (DRINKS, 'Drinks'),
        (SALADS, 'Salads'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=MAINS,
    )
    # ----CATEGORY-END---->

    # ----TYPE------------>
    VEGE = 'VEGE'
    VEGA = 'VEGA'
    MEAT = 'MEAT'
    TYPE_CHOICES = [
        (VEGE, 'Vegetarian'),
        (VEGA, 'Vegan'),
        (MEAT, 'Meat'),
    ]
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=MEAT)
    # ----TYPE----END------->

    hot = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(default='Description: ')
    image = models.ImageField(default='', upload_to='static/assets/img/products')
    # for these many persons
    size = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.IntegerField(default=0)


class Customer(models.Model):
    user = models.OneToOneField(User, default='2', on_delete=models.CASCADE)
    phone_number = models.CharField(default=' ', max_length=20)
    address = models.TextField(default=' ')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # other fields

