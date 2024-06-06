class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product(id = {self.product_id}, name = {self.name}, price = {self.price})'
