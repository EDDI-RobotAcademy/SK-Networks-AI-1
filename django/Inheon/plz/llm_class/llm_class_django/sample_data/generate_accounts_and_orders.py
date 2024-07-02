import os
import django
import random
from django.db import transaction

from account.entity.account import Account
from account.entity.profile import Profile

# Django settings 모듈 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "llm_class_django.settings")
django.setup()

from orders.entity.orders import Orders
from orders.entity.orders_item import OrdersItem
from orders.entity.orders_status import OrderStatus
from product.entity.models import Product


# Fetch all available products
products = list(Product.objects.all())
account_ids = list(Account.objects.values_list('id', flat=True))


def create_account(login_type_id, role_type_id, nickname, email):
    # Ensure nickname is unique
    unique_nickname = nickname
    count = 1
    while Profile.objects.filter(nickname=unique_nickname).exists():
        unique_nickname = f"{nickname}_{count}"
        count += 1

    account = Account.objects.create(loginType_id=login_type_id, roleType_id=role_type_id)
    Profile.objects.create(id=account.id, nickname=unique_nickname, email=email, account_id=account.id)
    return account.id


def create_random_order(account_id):
    try:
        with transaction.atomic():
            order = Orders.objects.create(account_id=account_id, status=OrderStatus.PENDING)

            # Determine the number of items in this order (Normal distribution around 3 items, std dev of 1)
            num_items = int(random.gauss(3, 1))
            num_items = max(1, min(num_items, 5))  # Clamp between 1 and 5 items

            for _ in range(num_items):
                product = random.choice(products)
                quantity = int(random.gauss(5, 2))  # Normal distribution around 5 quantity, std dev of 2
                quantity = max(1, min(quantity, 10))  # Clamp between 1 and 10 quantities
                price = product.productPrice

                OrdersItem.objects.create(
                    orders=order,
                    product=product,
                    price=price,
                    quantity=quantity
                )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")


# Create accounts if less than 7
if len(account_ids) < 7:
    for i in range(len(account_ids), 7):
        nickname = f"User{i + 1}"
        email = f"user{i + 1}@example.com"
        account_id = create_account(1, 1, nickname, email)
        account_ids.append(account_id)

# Generate 10,000 orders
for _ in range(10000):
    account_id = random.choice(account_ids)
    create_random_order(account_id)

print("Sample data generation completed.")
