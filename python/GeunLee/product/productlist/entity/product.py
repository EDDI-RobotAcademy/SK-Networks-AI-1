class Product:

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def getName(self):
        return self.product_name

    def getPrice(self):
        return self.product_price
