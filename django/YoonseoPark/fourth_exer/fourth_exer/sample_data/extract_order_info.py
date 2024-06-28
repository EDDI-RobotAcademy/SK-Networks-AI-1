from orders.entity.orders_item import OrdersItem
import pandas as pd

def export_orders_to_excel(file_path):
    orders_items = OrdersItem.objects.select_related('orders', 'product').all()

    data = []
    for order_item in orders_items:
        order = order_item.orders
        product = order_item.product
        data.append({
            'accountId': order.account_id,
            'productId': product.productId,
            'quantity': order_item.quantity,
            'price': order_item.price
        })

    df = pd.DataFrame(data)

    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Exported orders data to {file_path}")

file_path = "orders_data.xlsx"
export_orders_to_excel(file_path)
