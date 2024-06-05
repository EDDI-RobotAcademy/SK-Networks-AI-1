from product.service.product_service_impl import ProductServiceImpl


class DomainInitializer:

    @staticmethod
    def initPlayerDomain():
        ProductServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()