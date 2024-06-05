from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # @Autowired
            # private GameRepository gameRepository
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
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

        # 2명의 주사위 결과
        # hash로 만들어줌
        playerDiceMap = {player.getPlayerNickname() : dice.getDiceNumber() for player, dice in zip(playerList, diceList)}
        print(playerDiceMap)

        # 승자 발표 >> 무승부 처리 필요
        # hash에 get을 해주면 value값이 반환됨
        maxDicePlayer = max(playerDiceMap, key=playerDiceMap.get) # max에 key값 넣을 수도 있구나..
        print(f"승자 {maxDicePlayer}")

        # 게임결과 저장을 위함 -> 게임결과 나중에 game entity에 넣기
        self.__gameRepository.save(playerDiceMap)


