import os
from product.entity.models import Product
from product.repository.product_repository import ProductRepository
from manual_proj import settings


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
        return Product.objects.all().order_by('prodname')

    def create(self, prodname, price, writer, content, productImage):

        uploadDirectory='C:/sk_project/SK-Networks-AI-1/ui/minji-choi/product_ui/src/assets/images/uploadImages'

        os.makedirs(uploadDirectory, exist_ok=True)

        imagePath = os.path.join(uploadDirectory, productImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in productImage.chunks():
                destination.write(chunk)

        product = Product(
            prodname = prodname,
            content = content,
            writer = writer,
            price = price,
            productImage = productImage.name
        )
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