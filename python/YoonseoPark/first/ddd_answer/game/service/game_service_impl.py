from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService



class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def makeGame(self, playerId1, playerId2):
        self.__gameRepository.getGameResult(playerId1,playerId2)

