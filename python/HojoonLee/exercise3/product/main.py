from initializer.domain_initializer import DomainInitializer
from product.service.product_service_impl import ProductServiceImpl

DomainInitializer.initEachDomain()

if __name__ == "__main__":

    product_service = ProductServiceImpl.getInstance()
    # service 기능을 2번 호출 안 한건 좋음, product_service.getProductList() 이후 부르면 x (재혁 리뷰 참고)
    product_service.displayProductList()
