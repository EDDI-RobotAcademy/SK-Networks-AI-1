# 데이터저장, 검색 데이터를 저장하고 반환할수있게한다.
class ProductRepository:
    def __init__(self):
        self.products = []
    def add(self, product):
        self.products.append(product)
    def list_all(self):
        return self.products
