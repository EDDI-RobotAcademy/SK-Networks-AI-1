from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

# Alt + Insert
# Implement
# Implement List Interface


class PlayerRepositoryImpl(PlayerRepository):

    # __instance는 실질적으로 DicdRepository 구현체가 존재하느냐 마느냐를 보는 부분입니다.
    __instance = None

    # __new__ 를 보면 제일 이상한 부분이 보이는데 cls라는 것입니다.
    # 도대체 cls가 머임??
    # 보편적으로 cls는 클래스와 매서드가 서로 참조하기 위해 사용하는 내부 인자(??ㅋㅋ 정신 나갈거 같애)
    # self랑은 무슨 관계지? 라는 생각이 보편적으로 들 수 있습니다.
    # 원래 self를 통해 접근 할 수 있었잖아
    # 근데 지금 만들고 있는 클래스는 그런 self 인자가 없단 말이지
    # 이럴 때 접근할 수 있게 해주는게 cls임

    # 원래 객체화가 되었다면 self를 사용했겠지만
    # __new__() 를 진행하는 과정에서 아직 객체화가 완료되이 않았습니다.
    # 그렇기 때문에 self를 사용할 수 없는데 이 시점에 클래스 자체에 접근할 수 있는 인자가 바로 cls입니다.
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # super(): parent 클래스를 생성합니다.
            cls.__instance.__playerList = []

        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, nickname):
        player = Player(nickname)
        self.__playerList.append(player)

    def findPlayerByNickname(self, nickname):
        pass
