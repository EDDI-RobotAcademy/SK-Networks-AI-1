# Generated by Django 5.0.6 on 2024-06-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("productId", models.AutoField(primary_key=True, serialize=False)),
                ("productName", models.CharField(max_length=128)),
                ("price", models.IntegerField()),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]
