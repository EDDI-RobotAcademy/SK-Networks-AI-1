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
        maxDicePlayer = max(playerDiceMap, key=playerDiceMap.get) # 해쉬에 get하면 value값 나옴
        print(playerDiceMap)

        if maxDicePlayer == min(playerDiceMap, key=playerDiceMap.get):
            print('무승부!!')
        else:
            print(f'{maxDicePlayer} win!')

        self.__gameRepository.save(playerDiceMap)