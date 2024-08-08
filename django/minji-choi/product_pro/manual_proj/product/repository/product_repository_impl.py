import os
from product.entity.product import Product
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
        return Product.objects.all().order_by('productName')

    def create(self, productName, productPrice, writer, productCategory, content, productImage):

        uploadDirectory='C:/sk_project/SK-Networks-AI-1/ui/minji-choi/product_ui/src/assets/images/uploadImages'

        os.makedirs(uploadDirectory, exist_ok=True)

        imagePath = os.path.join(uploadDirectory, productImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in productImage.chunks():
                destination.write(chunk)

        product = Product(
            productName=productName,
            content=content,
            writer=writer,
            productPrice=productPrice,
            productCategory=productCategory,
            productImage=productImage.name
        )
        product.save()
        return product

    def findByProductId(self, productId):
        try:
            return Product.objects.get(productId=productId)
        except Product.DoesNotExist:
            return None

    def deleteByProductId(self, productId):
        product = Product.objects.get(productId=productId)
        product.delete()

    def update(self, product, productData):
        for key, value in productData.items():
            print(f"key={key}, value={value}")
            setattr(product, key, value)
        product.save()
        return product