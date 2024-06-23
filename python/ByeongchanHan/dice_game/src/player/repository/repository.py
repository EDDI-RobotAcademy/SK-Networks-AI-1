import abc


class PlayerRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, nickname):
        pass

    @abc.abstractmethod
    def get_player_by_nickname(self, nickname):
        pass

    @property
    @abc.abstractmethod
    def player_list(self):
        pass
