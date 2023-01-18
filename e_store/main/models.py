from django.db import models

# def product_image_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/products/<product_name>/<filename>
#     return 'products/{0}/{1}'.format(instance.name, filename)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comments = models.IntegerField()
    brand = models.CharField(max_length=255)
    description = models.TextField()
    available_colors = models.CharField(max_length=255)
    specification = models.TextField()
    image = models.ImageField(default='', upload_to='assets/img/products/')


