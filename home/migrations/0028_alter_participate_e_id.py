# Generated by Django 4.2.10 on 2024-02-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0027_participate_e_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participate", name="e_id", field=models.TextField(),
        ),
    ]
