from src.player.repository import PlayerRepositoryImpl

from .service import PlayerService


class PlayerServiceImpl(PlayerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__player_repository = PlayerRepositoryImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create_player(self, nickname):
        try:
            self.__player_repository.create(nickname)
        except Exception as e:
            raise Exception from e

    def find_player_by_nickname(self, nickname):
        return self.__player_repository.find_player_by_nickname(nickname)

    @property
    def player_list(self):
        return self.__player_repository.player_list
