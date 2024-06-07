from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService



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
        for dice in diceList:
            print(f"주사위 눈금: {dice.getDiceNumber()}")

        playerList = self.__playerRepository.list()
        playerDiceMap = {player.getPlayerNickname(): dice.getDiceNumber() \
                         for player, dice in zip(playerList, diceList)}

        self.__gameRepository.save(playerDiceMap)

    def checkDiceGameWinner(self):
        # SW를 개발 할 때는 당장 눈 앞의 결과도 중요하지만
        # 비즈니스 지속성을 위해 미래 또한 고려하지 않을 수 없습니다.
        # 그러므로 '왜 이런 쓸모 없는 행위를 하는 것이지 ?' 라는 관점이 아닌
        # 추후 이 부분이 확장 될 때 어떤 Domain과 협력할지 보장 할 수 없기 때문에
        # 아래와 같이 단순히 Repository를 호출하는 경우에도
        # Service, Repository Layer를 구성합니다.
        # 한마디로 요약하자면: 확장성
        self.__gameRepository.checkDiceGameWinner()



