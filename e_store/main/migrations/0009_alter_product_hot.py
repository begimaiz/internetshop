# Generated by Django 4.1.5 on 2023-01-26 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_product_hot_product_type_alter_product_comments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="hot",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]