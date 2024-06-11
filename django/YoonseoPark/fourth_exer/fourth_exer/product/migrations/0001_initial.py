
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
                ("productPrice", models.DecimalField(max_digits=10, decimal_places=2)),
                ("productDescription", models.TextField()),
                ("registeredDate", models.DateTimeField(auto_now_add=True)),
                ("updatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]
