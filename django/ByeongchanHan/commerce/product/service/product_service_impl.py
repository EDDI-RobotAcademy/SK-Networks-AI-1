from product.service.product_service import ProductService
from product.repository.product_repository_impl import ProductRepositoryImpl


class ProductServiceImpl(ProductService):
    product_repo_impl = ProductRepositoryImpl()

    def list(self):
        return self.product_repo_impl.list()

    def create_product(self, product_data):
        self.product_repo_impl.create(product_data)

    def update_product(self, product_id, update_data):
        self.product_repo_impl.update(product_id, update_data)

    def read_product(self, product_id):
        return self.product_repo_impl.find_by_id(self, product_id)

    def delete_product(self, product_id):
        self.product_repo_impl.delete_by_id(product_id)
