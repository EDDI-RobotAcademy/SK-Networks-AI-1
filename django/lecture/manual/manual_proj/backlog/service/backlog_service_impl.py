from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog.service.backlog_service import BacklogService





class BacklogServiceImpl(BacklogService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklog(self, title):
        try:
            return self.__backlogRepository.create(title)

        except Exception as e:
            print('Error creating order:', e)
            raise e