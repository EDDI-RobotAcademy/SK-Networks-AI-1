from product.entity.models import Product
from product.repository.product_repository import ProductRepository


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
        # print(f"list() -> Product", Product)
        # print(f"list() -> Product.objects", Product.objects)
        # print(f"list() -> Product.objects.all()", Product.objects.all())
        #
        # productList = Product.objects.all()
        # for product in productList:
        #     print(f"Product: {product}")

        return Product.objects.all().order_by('prodname')

    def create(self, productData):
        product = Product(**productData)
        product.save()
        return product
    def findByProductId(self, productId):
        return Product.objects.get(productId=productId)

    def deleteByProductId(self, productId):
        product = Product.objects.get(productId=productId)
        product.delete()

    def update(self, product, productData):
        for key, value in productData.items():
            print(f"key={key}, value={value}")
            setattr(product, key, value)
        product.save()
        return product