from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):

    __instance = None # 객체가 있냐없냐 구분자

    # 싱글톤 만들기
    def __new__(cls):
        if cls.__instance is None: # 객체가 없다면 생성하기
            cls.__instance = super().__new__(cls) # 부모객체 상속
            cls.__playerlist = []
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    # 추상화부분 구현하기
    def match(self, playerId,playerNickname):
        player = Player()
        player.setPlayerId(playerId)
        player.setPlayerNickname(playerNickname)  # 이 부분은 어떻게 받아주면 좋을까?
        self.__playerlist.append(player)

    # def getPlayerId(self, playerId):


    def getPlayerId(self, playerId):
        for player in self.__playerlist:
            # 여기서의 getPlayerId에 입력이 필요하지 않은 이유는 Player class의 getPlayerId기 때문에 필요가 없는것! (중요)
            if player.getPlayerId() == playerId:
                #return player # 해당 객체 반환
                return player.getPlayerId()
        return None

    def getPlayerNickname(self, playerId):
        #return [dice.getDiceNumber() for dice in self.__dicelist if dice.getPlayerId() == playerId]
        return [player.getPlayerNickname() for player in self.__playerlist if player.getPlayerId()==playerId]


