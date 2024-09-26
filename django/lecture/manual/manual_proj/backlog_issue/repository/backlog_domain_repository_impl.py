from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_issue.entity.backlog_issue import BacklogIssue
from backlog_issue.repository.backlog_domain_repository import BacklogIssueRepository


class BacklogIssueRepositoryImpl(BacklogIssueRepository):
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

    def create(self, backlog, issue):
        try:
            backlogIssue = BacklogIssue(backlog=backlog, issue=issue)
            backlogIssue.save()

            return backlogIssue

        except IntegrityError:
            return None

    def modify(self, backlog, issue):
        try:
            backlogIssue = BacklogIssue.objects.get(backlog=backlog)

            backlogIssue.issue = issue
            backlogIssue.save()
            return backlogIssue

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
