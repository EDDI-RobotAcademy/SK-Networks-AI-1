from account.repository.account_repository import AccountRepository
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType
from account.entity.account import Account


class AccountRepositoryImpl(AccountRepository):
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

    def create(self, loginType, roleType):
        # '_': 보편적으로 언더바는 별 의미가 없는 데이터를 받는 경우 사용하지 않는다는 의미의 관습적 표현
        loginTypeEntity, _ = AccountLoginType.objects.get_or_create(loginType=loginType)
        roleTypeEntity, _ = AccountRoleType.objects.get_or_create(roleType=roleType)

        account = Account.objects.create(loginType=loginTypeEntity, roleType=roleTypeEntity)
        return account