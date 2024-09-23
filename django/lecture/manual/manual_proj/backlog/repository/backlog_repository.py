from abc import ABC, abstractmethod


class BacklogRepository(ABC):
    @abstractmethod
    def create(self, title):
        pass
