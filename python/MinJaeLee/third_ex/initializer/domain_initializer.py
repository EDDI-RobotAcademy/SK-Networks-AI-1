from product.service.product_service_impl import productServiceImpl


class DomainInitializer:
    @staticmethod
    def initProductDomain():
        productServiceImpl.getInstance()
    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductDomain()
