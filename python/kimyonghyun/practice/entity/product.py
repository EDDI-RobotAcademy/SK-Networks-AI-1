class Product:
    __productId = 0
    __autoIncrementProductId = 0

    def __init__(self,productname):
        Product.__autoIncrementProductId+=1
        self.__productId = Product.__autoIncrementProductId
        self.__productname = productname

    def getProductId(self):
        return self.__productId

    def getProductName(self):
        return self.__productname
