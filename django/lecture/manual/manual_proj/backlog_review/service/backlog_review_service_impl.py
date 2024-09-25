from backlog.repository.backlog_repository_impl import BacklogRepositoryImpl
from backlog_review.repository.backlog_review_repository_impl import BacklogReviewRepositoryImpl
from backlog_review.service.backlog_review_service import BacklogReviewService


class BacklogReviewServiceImpl(BacklogReviewService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__backlogRepository = BacklogRepositoryImpl.getInstance()
            cls.__instance.__backlogReviewRepository = BacklogReviewRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBacklogReview(self, backlogId, review):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogReviewRepository.create(backlog, review)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e

    def modifyBacklogReview(self, backlogId, review):
        try:
            backlog = self.__backlogRepository.findById(backlogId)

            if not backlog:
                raise ValueError(f"Backlog with id {backlogId} does not exist")

            return self.__backlogReviewRepository.modify(backlog, review)

        except Exception as e:
            print('Error creating backlog:', e)
            raise e
