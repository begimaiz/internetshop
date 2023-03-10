# Generated by Django 4.1.5 on 2023-01-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
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
