import random

from django.db import transaction
from account.entity.account import Account
from orders.entity.orders_item import OrdersItem
from product.entity.models import Product
from account.entity.profile import Profile
from orders.entity.orders import Orders
from orders.entity.orders_status import OrdersStatus

products = list(Product.objects.all())
account_ids = list(Account.objects.values_list('id', flat=True))

def create_account(login_type_id, role_type_id, nickname, email):
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
            order = Orders.objects.create(account_id=account_id, status=OrdersStatus.PENDING)

            num_items = int(random.gauss(3,1))
            num_items = max(1,min(num_items,5)) # clamp between 1 ~ 5

            for _ in range(num_items):
                product = random.choice(products)
                quantity = int(random.gauss(5,2))
                quantity = max(1, min(quantity,10))
                price = product.productPrice

                OrdersItem.objects.create(
                    orders=order,
                    product=product,
                    price=price,
                    quantity=quantity
                )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")

if len(account_ids) < 7 :
    for i in range(len(account_ids), 7):
        nickname = f"User{i + 1}"
        email = f"user{i+1}@example.com"
        account_id = create_account(1,1,nickname,email)
        account_ids.append(account_id)

for _ in range(10000):
    account_id = random.choice(account_ids) # 계정 id 랜덤으로 선택
    create_random_order(account_id) # 선택한 계정에 대해 주문을 작성

print("sample data generation completed")
