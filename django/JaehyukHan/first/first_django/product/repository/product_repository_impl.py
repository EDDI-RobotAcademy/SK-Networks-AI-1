import os

from first_django import settings
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
        return Product.objects.all().order_by('registeredDate')

    def create(self, productName, productPrice, productDescription, productImage):
        # uploadDirectory = os.path.join(
        #     settings.BASE_DIR,
        #     '../../../../ui/JaehyukHan/first/src/assets/images/uploadImages')
        uploadDirectory = r"/Users/j213h/Documents/Python/SKN AI Camp/proj/SK-Networks-AI-1/ui/JaehyukHan/first/src/assets/images/uploadImages"

        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, productImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in productImage.chunks():
                destination.write(chunk)

        product = Product(
            productName=productName,
            productPrice=productPrice,
            productDescription=productDescription,
            productImage=productImage.name
        )
        product.save()
        return product


