from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType
from account.repository.account_repository import AccountRepository


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
        loginTypeEntity, _ = AccountLoginType.objects.get_or_create(loginType=loginType)
        roleTypeEntity, _ = AccountRoleType.objects.get_or_create(roleType=roleType)

        account = Account.objects.create(loginType=loginTypeEntity, roleType=roleTypeEntity)
        return account

    def findById(self, accountId):
        account = Account.objects.get(id=accountId)
        return account