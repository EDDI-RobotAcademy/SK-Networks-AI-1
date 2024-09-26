
from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_domain.repository.backlog_domain_repository_impl import BacklogDomainRepositoryImpl
from backlog_domain.service.backlog_domain_service import BacklogDomainService


class BacklogDomainServiceImpl(BacklogDomainService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogDomainRepository = BacklogDomainRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogDomain(self, backlogId, domain):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogDomainRepository.create(backlog, domain)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogDomain(self, backlogId, domain):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogDomainRepository.modify(backlog, domain)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
