from abc import ABC, abstractmethod


class BacklogMapNumberRepository(ABC):
    @abstractmethod
    def create(self, backlog, backlogMapNumber):
        pass

    @abstractmethod
    def modify(self, backlog, backlogMapNumber):
        pass
