from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__player_list = []
        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def add_player(self, player_id, nickname):
        player = Player(player_id, nickname)
        self.__player_list.append(player)

    def get_player_by_id(self, player_id):
        for player in self.__player_list:
            if player.get_player_id() == player_id:
                return player
        return None