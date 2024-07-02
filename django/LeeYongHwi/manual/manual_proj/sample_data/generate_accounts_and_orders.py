import random

from django.db import transaction

from account.entity.account import Account
from account.entity.profile import Profile
from orders.entity.orders import Orders
from orders.entity.orders_item import OrdersItem
from orders.entity.orders_status import OrderStatus
from product.entity.models import Product

productList = list(Product.objects.all())
accountIdList = list(Account.objects.values_list('id', flat=True))


def createAccount(loginTypeId, roleTypeId, nickname, email):
    uniqueNickname = nickname
    count = 1
    while Profile.objects.filter(nickname=uniqueNickname).exists():
        uniqueNickname = f"{nickname}_{count}"
        count += 1

    account = Account.objects.create(loginType_id=loginTypeId, roleType_id=roleTypeId)
    Profile.objects.create(id=account.id, nickname=uniqueNickname, email=email, account_id=account.id)
    return account.id


def createRandomOrder(account_id):
    try:
        with transaction.atomic():
            order = Orders.objects.create(account_id=account_id, status=OrderStatus.PENDING)

            numItems = int(random.gauss(3, 1))
            numItems = max(1, min(numItems, 5))

            for _ in range(numItems):
                product = random.choice(productList)
                quantity = int(random.gauss(5, 2))
                quantity = max(1, min(quantity, 10))
                price = product.productPrice

                OrdersItem.objects.create(
                    orders=order,
                    product=product,
                    price=price,
                    quantity=quantity
                )
    except Exception as e:
        print(f"Error creating order for account {account_id}: {e}")


if len(accountIdList) < 7:
    for i in range(len(accountIdList), 7):
        nickname = f"User{i + 1}"
        email = f"user{i + 1}@example.com"
        accountId = createAccount(1, 1, nickname, email)
        accountIdList.append(accountId)

for _ in range(10000):
    accountId = random.choice(accountIdList)
    createRandomOrder(accountId)

print("Sample data generation completed.")
