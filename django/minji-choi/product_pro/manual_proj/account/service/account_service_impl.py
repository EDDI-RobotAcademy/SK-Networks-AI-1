from account.service.account_service import AccountService
from manual_proj import settings
import requests
from account.repository.profile_repository_impl import ProfileRepositoryImpl

class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def checkEmailDuplication(self, email):
        print("service checkEmailDuplication()")
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None

