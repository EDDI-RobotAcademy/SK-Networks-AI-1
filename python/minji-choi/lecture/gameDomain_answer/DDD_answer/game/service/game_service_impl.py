from game.service.game_service import GameService
from game.repository.game_repository_impl import GameRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl

class GameServiceImpl(GameService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # 여기에 먼저 다이스, 게임, 플레이어 레포지토리 instance get

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
        for d in diceList:
            print(f'DiceNumber : {d.getDiceNumber()}')

        playerList = self.__playerRepository.getList()

        playerDiceMap = {player.getNickname():dice.getDiceNumber() for player, dice in zip(playerList, diceList)} # 해쉬를 만든것
        self.__gameRepository.save(playerDiceMap)


    def checkDiceGameWinner(self):
        # sw를 개발할 때는 당장 눈 앞의 결과도 중요하지만 비즈니스의 지속성을 위해 미래 또한 고려해야 한다.
        # 그러므로 단순히 winner를 뽑는 이 행위가 추후 확장 될 때 어떤 domain과 협력할지 보장할 수 없기 떄문에 아래와 같이 단순히 레피지토리를
        # 호출하는 경우에도 service, repository layer를 구축합니다. 한 마디로 확장성을 고려한 것
        self.__gameRepository.checkDiceGameWinner()
