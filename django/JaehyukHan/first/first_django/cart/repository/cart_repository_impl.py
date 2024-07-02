from cart.repository.cart_repository import CartRepository

from cart.entity.cart import Cart


class CartRepositoryImpl(CartRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findByAccount(self, account):
        try:
            cart = Cart.objects.get(account=account)
            return cart

        except Cart.DoesNotExist:
            print('accountId로 카트를 찾을 수 없음!')
            return None

        except Exception as e:
            print('accountId로 카트 찾는 중 에러 발생:', e)
            return None

    def register(self, account):
        # 내가 작성한 코드
        # cart = Cart(account=account)
        # cart.save()
        # return cart
        # 강사님 코드 비교
        return Cart.objects.create(account=account)
