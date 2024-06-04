from game.service.game_service import GameService
from game.repository.game_repository_impl import GameRepositoryImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl



class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def playGame(self, firstPlayer, secondPlayer):
        self.__diceRepository.rollDice(firstPlayer)
        self.__diceRepository.rollDice(secondPlayer)


    def findWinner(self, firstPlayer, secondPlayer):
        firstPlayerScore = self.__diceRepository.checkDice(firstPlayer)
        secondPlayerScore = self.__diceRepository.checkDice(secondPlayer)
        # print(firstPlayer.getPlayerId(), secondPlayer.getPlayerId())
        # print(firstPlayerScore, secondPlayerScore)
        if firstPlayerScore > secondPlayerScore:
            return firstPlayer

        elif firstPlayerScore < secondPlayerScore:
            return secondPlayer

        else:
            return None
