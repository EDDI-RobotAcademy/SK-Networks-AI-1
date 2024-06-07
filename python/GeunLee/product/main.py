from productlist.service.product_list_service_impl import ProductListServiceImpl
from initializer.domain_initializer import DomainInitializer

if __name__ == "__main__":
    DomainInitializer.initEachDomain()

    productService = ProductListServiceImpl.getInstance()
    productList = productService.getProductList()

    for product in productList:
        print(f"상품명: {product.getName()}, 가격: {product.getPrice()}")
