from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.service.game_service import GameService
from dice.repository.dice__repository__impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def registerGameResult(self):
        self.__diceRepository.rollDice()
        self.__diceRepository.rollDice()

        diceList = self.__diceRepository.getDiceList()
        for dice in diceList:
            print(f"dice number: {dice.getDiceNumber()}")

        playerList = self.__playerRepository.list()
        playerDiceMap = {player.getPlayerNickname(): dice.getDiceNumber()\
                          for player, dice in zip(playerList,diceList)}

        self.__gameRepository.save(playerDiceMap)
    def checkDiceGameWinner(self):
        # 이 코드를 작성한 이유는 지금 당장은 도메인 참조를 안하는데
        # 나중에 코드가 확장되다 보면 추후 확장 시에 편하게 확장할 수 있다.
        self.__gameRepository.checkDiceGameWinner()

