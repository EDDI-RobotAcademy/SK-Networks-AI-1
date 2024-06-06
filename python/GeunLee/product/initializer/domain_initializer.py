from productlist.service.product_list_service_impl import ProductListServiceImpl


class DomainInitializer:
    @staticmethod
    def initProductListDomain():
        ProductListServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initProductListDomain()
