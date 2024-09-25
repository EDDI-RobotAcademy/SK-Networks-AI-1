from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog.entity.backlog_domain import BacklogDomain
from backlog.repository.backlog_domain_repository import BacklogDomainRepository


class BacklogDomainRepositoryImpl(BacklogDomainRepository):
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

    def create(self, domain):
        try:
            backlogDomain = BacklogDomain(domain=domain)
            backlogDomain.save()

            return backlogDomain

        except IntegrityError:
            return None

    def modify(self, backlog, domain):
        try:
            backlogDomain = BacklogDomain.objects.get(backlog=backlog)

            backlogDomain.domain = domain
            backlogDomain.save()
            return backlogDomain

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
