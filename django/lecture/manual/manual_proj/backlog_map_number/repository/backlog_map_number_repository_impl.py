from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_domain.entity.backlog_domain import BacklogDomain
from backlog_map_number.entity.backlog_map_number import BacklogMapNumber
from backlog_map_number.repository.backlog_map_number_repository import BacklogMapNumberRepository


class BacklogMapNumberRepositoryImpl(BacklogMapNumberRepository):
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

    def create(self, backlog, backlogMapNumber):
        try:
            backlogMapNumber = BacklogMapNumber(backlog=backlog, map_number=backlogMapNumber)
            backlogMapNumber.save()

            return backlogMapNumber

        except IntegrityError:
            return None

    def modify(self, backlog, backlogMapNumber):
        try:
            backlogMapNumber = BacklogDomain.objects.get(backlog=backlog)

            backlogMapNumber.map_number = backlogMapNumber
            backlogMapNumber.save()
            return backlogMapNumber

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
