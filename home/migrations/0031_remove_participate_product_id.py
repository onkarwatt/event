# Generated by Django 4.2.10 on 2024-02-10 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0030_rename_ratings_products_link"),
    ]

    operations = [
        migrations.RemoveField(model_name="participate", name="product_id",),
    ]