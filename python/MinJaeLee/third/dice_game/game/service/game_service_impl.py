from dice_game.dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice_game.game.service.game_service import GameService
from dice_game.player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # @Autowired
            # private GameRepository gameRepository
            # cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

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
        playerList = self.__playerRepository.list()

        for n in range(len(diceList)):
            print(f'player nickname: {playerList[n].getPlayerNickname()}')
            print(f'dice number: {diceList[n].getDiceNumber()}')
            print()

