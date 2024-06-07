"""
player_repository에서 player를 참조함


"""
from player.repository.player_repository import PlayerRepository
from player.entity.player import Player


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # dice와 같이 구현함
            cls.__instance.__playerList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def create(self, nickname):
        # 'nickname'이라는 Player를 생성
        player = Player(nickname)
        self.__playerList.append(player)

    def findPlayerByNickname(self, nickname):
        # self.__diceList에서 playerId로 찾는 것과 동일
        for player in self.__playerList:
            if player.getPlayerNickname() == nickname:
                return player

        return None




