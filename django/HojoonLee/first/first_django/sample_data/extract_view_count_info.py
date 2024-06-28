import os
import random

import django
import pandas as pd

from account.entity.account import Account
from product.entity.models import Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_django.settings")
django.setup()

def generate_and_export_view_counts(filePath):
    accountList = list(Account.objects.all())
    productList = list(Product.objects.all())

    data = []

    for account in accountList:
        for product in productList:
            viewCount = random.randint(1000, 10000)

            data.append({
                'accountId':account.id,
                'productId':product.productId,
                'viewCount': viewCount
            })

    df = pd.DataFrame(data)
    df.to_excel(filePath, index=False, engine='openpyxl')

    print(f"조회수 추출 완료: {filePath}")

filePath = "view_counts_data.xlsx"
generate_and_export_view_counts(filePath)