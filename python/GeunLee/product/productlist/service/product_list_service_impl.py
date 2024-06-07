from productlist.repository.product_list_repository_impl import (
    ProductListRepositoryImpl,
)
from productlist.service.product_list_service import ProductListService


class ProductListServiceImpl(ProductListService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__productlistRepository = (
                ProductListRepositoryImpl().getInstance()
            )

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getProductList(self):
        return self.__productlistRepository.getProductList()
