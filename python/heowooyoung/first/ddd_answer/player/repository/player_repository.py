from abc import ABC, abstractmethod

class PlayerRepository(ABC):
    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def get_player_by_id(self, player_id):
        pass