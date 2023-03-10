# Generated by Django 4.1.5 on 2023-01-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_product_hot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("AL", "All"),
                    ("MA", "Mains"),
                    ("SO", "Soups"),
                    ("SI", "Sides"),
                    ("DE", "Desserts"),
                    ("DR", "Drinks"),
                    ("SA", "Salads"),
                ],
                default="MA",
                max_length=2,
            ),
        ),
    ]
