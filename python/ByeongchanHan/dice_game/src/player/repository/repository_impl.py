from src.player.entity import Player

from .player_error import PlayerExistsError
from .repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__player_dict = {}

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, nickname):
        player = Player(nickname)

        if nickname in self.__player_dict:
            raise PlayerExistsError("Nickname already exists!")

        self.__player_dict[nickname] = player

    def get_player_by_nickname(self, nickname):
        self.__player_dict.get(nickname, None)

    @property
    def player_list(self):
        return list(self.__player_dict.values())
