from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Product

admin.site.register(Product)

LogEntry.objects.user = 'main.CustomUser'
