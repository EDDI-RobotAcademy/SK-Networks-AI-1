from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_map_number.repository.backlog_map_number_repository_impl import BacklogMapNumberRepositoryImpl
from backlog_map_number.service.backlog_map_number_service import BacklogMapNumberService


class BacklogMapNumberServiceImpl(BacklogMapNumberService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogMapNumberRepository = BacklogMapNumberRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogMapNumber(self, backlogId, backlogMapNumber):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogMapNumberRepository.create(backlog, backlogMapNumber)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogMapNumber(self, backlogId, backlogMapNumber):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogMapNumberRepository.modify(backlog, backlogMapNumber)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
