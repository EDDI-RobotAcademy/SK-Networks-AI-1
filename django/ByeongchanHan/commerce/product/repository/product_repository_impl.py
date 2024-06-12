from product.repository.product_repository import ProductRepository
from product.domain.models import Product


class ProductRepositoryImpl(ProductRepository):
    def find_by_id(self, product_id):
        return Product.objects.get(product_id=product_id)

    def create(self, product_data):
        product = Product(**product_data)
        product.save()
        return product

    def update(self, product_id, updated_data):
        product = self.find_by_id(product_id)
        for key, value in updated_data.items():
            setattr(product, key, value)
        product.save()
        return product

    def delete_by_id(self, product_id):
        product = self.find_by_id(product_id)
        product.delete()

    def list(self):
        return Product.objects.all().order_by("reg_date")
