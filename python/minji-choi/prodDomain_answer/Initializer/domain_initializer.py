from product.service.product_service_impl import ProductServiceImpl

class DomainInitializer:
    @staticmethod
    def initProductDomain():
        ProductServiceImpl.getInstance()
    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()
