from product.repository.product_repository import ProductRepository
from product.entity.models import Product


class ProductRepositoryImpl(ProductRepository):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Product.objects.all().order_by('regDate')

    def create(self, productData):
        product = Product(**productData)
        product.save() # 여기서 db에 create한 애가 저장됨
        return product

    def findByProductId(self, productId):
        return Product.objects.get(productId=productId)