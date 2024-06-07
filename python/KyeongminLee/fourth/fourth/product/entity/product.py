class Product:
    # 상품명, 가격, 상품 상세 정보
    product_name = None
    price = 0
    product_description = None

    def __init__(self, product_name, price, product_description):
        self.product_name = product_name
        self.price = price
        self.product_description = product_description

    def getProductName(self):
        return self.product_name

    def getPrice(self):
        return self.price

    def getProductDescription(self):
        return self.product_description