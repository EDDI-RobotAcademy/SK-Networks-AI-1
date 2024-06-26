import os
import django
import random
from django.db import transaction

from account.entity.account import Account
from account.entity.profile import Profile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from orders.entity.orders import Orders
from orders.entity.orders_item import OrdersItem
from orders.entity.orders_status import OrderStatus
from product.entity.models import Product

# Fetch all available products
products = list(Product.objects.all())
account_ids = list(Account.objects.values_list('id', flat=True))


def create_account(login_type_id, role_type_id, nickname, email):
    account = Account.objects.create(loginType_id=login_type_id, roleType_id=role_type_id)
    Profile.objects.create(id=account.id, nickname=nickname, email=email, account_id=account.id)
    return account.id


def create_random_order(account_id):
    try:
        with transaction.atomic():
            order = Orders.objects.create(account_id=account_id, status=OrderStatus.PENDING)

            # Determine the number of items in this order
            num_items = random.randint(1, 5)  # Each order will have between 1 to 5 items

            for _ in range(num_items):
                product = random.choice(products)
                quantity = random.randint(1, 10)  # Each item will have between 1 to 10 quantities
                price = product.price

                OrdersItem.objects.create(
                    orders=order,
                    product=product,
                    price=price,
                    quantity=quantity
                )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")


if len(account_ids) < 7:
    for i in range(len(account_ids), 7):
        nickname = f"User{i + 1}"
        email = f"user{i + 1}@example.com"
        account_id = create_account(1, 1, nickname, email)
        account_ids.append(account_id)

for _ in range(10000):
    account_id = random.choice(account_ids)
    create_random_order(account_id)

print("Sample data generation completed.")
