class Product:
    __productId = 0
    __autoIncrementProductId = 0

    def __init__(self, productName):
        Product.__autoIncrementProductId += 1
        self.__productId = Product.__autoIncrementProductId
        self.__productName = productName

    def getProductId(self):
        return self.__productId

    def getProductName(self):
        return self.__productName

