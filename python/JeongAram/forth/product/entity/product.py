# Entity를 작성하려고 보니까 놓친 부분이 생각 날 수 있습니다.
# 놓친 것이 무엇이나 하면 Product를 어떤 구성으로 만들 것이냐입니다.
# 요구사항이 명확하다면 이 부분이 어느정도 결정적이지만
# 요구사항이 없기 때문에 어떤 구성으로 할 것인지
# 만들면서 변할 수도 있습니다.

# ex) 만들다보니 사람들이 XXX 라는 기능을 좋아하는 것으로 판단됨
#     그래서 다른 이것을 좀 더 수월하게 가능하도록
#     엔티티 파트에 뭔가를 추가하는 작업이 발생 할 수도 있습니다.
#     단 엔티티 파일이 오염되면 안됨
class Product:
    # 상품명, 가격, 상품 상세 정보(이렇게 3가지만 다룹시다)
    product_name = None
    price = 0
    product_description = None

    def __init__(self, product_name, price, product_description):
        self.product_name= product_name
        self. price = price
        self.product_description = product_description

    def getProductName(self):
        return self.product_name

    def getPrice(self):
        return self.price

    def getProductDescription(self):
        return self.product_description
