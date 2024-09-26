from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_todo_check.entity.backlog_todo_check import BacklogTodoCheck
from backlog_todo_check.repository.backlog_todo_check_repository import BacklogTodoCheckRepository


class BacklogTodoCheckRepositoryImpl(BacklogTodoCheckRepository):
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

    def create(self, backlog, isChecked):
        try:
            backlogTodoCheck = BacklogTodoCheck(backlog=backlog, isChecked=isChecked)
            backlogTodoCheck.save()

            return backlogTodoCheck

        except IntegrityError:
            return None

    def modify(self, backlog, isChecked):
        try:
            backlogTodoCheck = BacklogTodoCheck.objects.get(backlog=backlog)

            backlogTodoCheck.isChecked = isChecked
            backlogTodoCheck.save()
            return backlogTodoCheck

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
