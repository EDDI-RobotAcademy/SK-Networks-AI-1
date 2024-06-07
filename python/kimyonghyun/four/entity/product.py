# entity를 작성하려고 보니까 놓친 부분이 있다.
# 요구 사항에 따라 구성이 변할 것
class product:
    product_name = None
    price = 0
    product_description = None

    def __init__(self,product_name,price,product_description):
        self.product_name = product_name
        self.price = price
        self.product_description = product_description

    def getProductName(self):
        return self.product_name

    def getPrice(self):
        return self.price

    def getProductDescription(self):
        return self.product_description

