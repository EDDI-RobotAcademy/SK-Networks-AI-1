import abc


class PlayerService(abc.ABC):
    @abc.abstractmethod
    def create_player(self, nickname):
        pass

    @abc.abstractmethod
    def find_player_by_nickname(self, nickname):
        pass

    @property
    @abc.abstractmethod
    def player_list(self):
        pass
