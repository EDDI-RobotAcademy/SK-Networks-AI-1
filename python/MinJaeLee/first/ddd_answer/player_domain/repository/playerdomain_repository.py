from abc import abstractmethod, ABC


class PlayerDomain_Repo(ABC):
    @abstractmethod
    def get_playerid_and_nickname(self, pid):
        pass