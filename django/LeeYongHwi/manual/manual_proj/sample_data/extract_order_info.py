from orders.entity.orders_item import OrdersItem
import pandas as pd


def exportOrdersToExcel(filePath):
    ordersItemList = OrdersItem.objects.select_related('orders', 'product').all()

    data = []
    for orderItem in ordersItemList:
        order = orderItem.orders
        product = orderItem.product
        data.append({
            'accountId': order.account_id,
            'productId': product.productId,
            'quantity': orderItem.quantity,
            'price': orderItem.price
        })

    df = pd.DataFrame(data)

    df.to_excel(filePath, index=False, engine='openpyxl')
    print(f"Exported orders data to {filePath}")

filePath = "orders_data.xlsx"
exportOrdersToExcel(filePath)