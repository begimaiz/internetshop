# Generated by Django 4.1.5 on 2023-01-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mycart", "0003_alter_cartitem_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="name",
            field=models.CharField(default="", max_length=20),
        ),
    ]
