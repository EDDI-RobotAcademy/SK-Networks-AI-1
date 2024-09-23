from backlog.repository.backlog_repository import BacklogRepository

from django.db import IntegrityError


class BacklogRepositoryImpl(BacklogRepository):
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

    def create(self, title):
        try:
            survey = Backlog(title=title)
            survey.save()

            return survey

        except IntegrityError:
            return None