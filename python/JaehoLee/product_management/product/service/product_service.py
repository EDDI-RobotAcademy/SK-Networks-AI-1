# 서비스는 로직처리 제품을
# 추가하고 나열하는기능.
from product.entity.product import Product
class ProductService:
    def __init__(self, repository):
        self.repository = repository
    def add_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.repository.add(product)
    def get_all_products(self):
        return self.repository.list_all()

