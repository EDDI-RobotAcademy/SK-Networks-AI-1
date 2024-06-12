# Generated by Django 5.0.6 on 2024-06-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("productId", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=32)),
                ("price", models.CharField(max_length=32)),
                ("product_description", models.TextField()),
                ("regDate", models.DateTimeField(auto_now_add=True)),
                ("updDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]