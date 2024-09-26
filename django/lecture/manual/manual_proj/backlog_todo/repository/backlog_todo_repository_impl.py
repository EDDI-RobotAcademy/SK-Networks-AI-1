from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_todo.entity.backlog_todo import BacklogTodo
from backlog_todo.repository.backlog_todo_repository import BacklogTodoRepository


class BacklogTodoRepositoryImpl(BacklogTodoRepository):
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

    def create(self, backlog, todo):
        try:
            backlogTodo = BacklogTodo(backlog=backlog, todo=todo)
            backlogTodo.save()

            return backlogTodo

        except IntegrityError:
            return None

    def modify(self, backlog, todo):
        try:
            backlogTodo = BacklogTodo.objects.get(backlog=backlog)

            backlogTodo.todo = todo
            backlogTodo.save()
            return backlogTodo

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
