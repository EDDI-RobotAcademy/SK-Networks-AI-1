from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameResult = {}

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, playerDiceMap):
        self.__gameResult = playerDiceMap

    def checkDiceGameWinner(self):
        maxDiceNumber = max(self.__gameResult.values())
        maxPlayerList = [player for player, diceNumber in self.__gameResult.items() \
                         if diceNumber == maxDiceNumber]

        if len(maxPlayerList) > 1:
            print("무승부입니다")
            return

        print(f"승자: {maxPlayerList[0]}")