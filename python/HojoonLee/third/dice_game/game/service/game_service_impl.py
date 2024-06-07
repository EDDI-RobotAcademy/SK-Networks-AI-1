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
        #maxDicePlayer = max(playerDiceMap, key=playerDiceMap.get) # max에 key값 넣을 수도 있구나..
        #print(f"승자 {maxDicePlayer}")

        # 게임결과 저장을 위함 -> 게임결과 나중에 game entity에 넣기
        self.__gameRepository.save(playerDiceMap)

    def checkDiceGameWinner(self):
        # Q) 위에 register는 중요한데 여기 check 부분은 굳이 service에서 부터 구현해야하나?
        # 저장할거면 repo에만 구현하면 되는데..
        # A) SW를 개발 할 때는 당장 눈앞의 결과도 중요하지만
        # 비즈니스 지속성을 위해 미래 또한 고려하지 않을 수 없습니다.
        # 그러므로 '왜 이런 쓸데 없는 행위를 하지?' 라는 관점이 아닌
        # 추후 이 부분이 확장 될 때 어떤 Domain과 협력할지 보장 할 수 없기 때문에
        # 아래와 같이 단순히 Repository를 호출하는 경우에도
        # Service, Repository Layer를 구성합니다.
        # 한 마디로 확장성 고려 (scailability)
        self.__gameRepository.checkDiceGameWinner() # 게임 repo의 checkWinner 함수 호출

