from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl

DomainInitializer.initEachDomain()


if __name__ == "__main__":
    productService = ProductServiceImpl.getInstance()
    productList = productService.productList()

    for product in productList:
        print(f"name: {product.getProductName()}, "
              f"price: {product.getPrice()}, "
              f"description: {product.getProductDescription()}")
