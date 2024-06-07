# Product를 어떤 구성으로 만들 것인지
# 요구사항이 없을 때는 어떤 구성으로 할 것인지 만들면서 변할 수 도
# ex. 사람들이 ~라는 기능을 좋아하는 것으로 판단돼서, 이것을 더 수월하게 가능하도록
# 엔티티 파트에 뭔가를 추가하는 작업이 발생하는 것. 단 엔티티의 오염은 x

class Product:
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

