from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_status.entity.backlog_status import BacklogStatus
from backlog_status.repository.backlog_status_repository import BacklogStatusRepository


class BacklogStatusRepositoryImpl(BacklogStatusRepository):
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

    def create(self, backlog, status):
        try:
            backlogStatus = BacklogStatus(backlog=backlog, status=status)
            backlogStatus.save()

            return backlogStatus

        except IntegrityError:
            return None

    def modify(self, backlog, status):
        try:
            backlog_status = BacklogStatus.objects.get(backlog=backlog)

            backlog_status.status = status
            backlog_status.save()
            return backlog_status

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog status found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
