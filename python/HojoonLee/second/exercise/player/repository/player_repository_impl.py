from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        # 근데 cls로 하면 무조건 __instance로 접근해야하는 것 같음 >> cls.__instance 까지가 객체화가 되었단 얘기
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerlist = [] # 여러 플레이어 객체를 담을 list
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:  # 해당 객체가 없다면
            cls.__instance = cls()  # 불러온 객체(cls)로 할당
        return cls.__instance

    def create(self, nickname):
        player = Player(nickname) # 여기서 Player class의 생성자를 활용
        self.__playerlist.append(player) # player 객체 저장

    def findPlayerByNickname(self, nickname):
        for player in self.__playerlist:
            if player.getPlayerNickname() == nickname:
                return player
        return None