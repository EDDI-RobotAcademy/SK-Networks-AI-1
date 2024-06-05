from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameResult = {} # hash니까 dict 형태로
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save(self, playerDiceMap):
        self.__gameResult = playerDiceMap # dict에 추가