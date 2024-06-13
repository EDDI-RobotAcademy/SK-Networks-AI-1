from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl


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
        for dice in diceList:
            print(f'dice number: {dice.getDiceNumber()}')

        playerList = self.__playerRepository.list()
        for player in playerList:
            print(f'player nickname: {player.getPlayerNickname()}')

        # self.__gameRepository.save()


