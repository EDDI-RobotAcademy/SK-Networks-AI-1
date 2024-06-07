from dice.entity.DiceNumber import DiceNumber
from dice.entity.dice import Dice
from player.repository.player_repository import PlayerRepository
import random

from player.entity.player import Player


# 파이썬의 상속은 아래와 같이 class A(상속할 클래스) 형태로 상속을 진행합니다.
# 인터페이스를 상속 받아서 가져온 클래스는 반드시 인터페이스 클래스에 있는 함수들을 만들어줘야 합니다.
class PlayerRepositoryImpl(PlayerRepository):
    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작
    # 싱글톤이 되면 객체는 유일성을 가지게 됩니다.
    # Entity에 있는 객체들은 여러 개가 될 수 있습니다.
    # 반면 이들을 서포트하는 Repository 객체나 Service 객체가 여러 개 존재 할 필요가 없습니다.
    # 그러므로 이들은 Singleton으로 구성하여 유일성을 가지게 만듭니다
    # 이것은 궁극적으로 메모리라는 자원을 좀 더 효율적으로 사용하기 위해 사용하는 기법입니다.
    # 관점으로 보자면 메모리 절감으로 보면 되겠습니다.
    __instance = None

    # 위의 __instance는 실질적으로 DiceRepository 구현체가 존재하느냐 마느냐를 보는 부분입니다.

    # __new__를 보면 제일 이상한 부분이 보이는데 cls라는 것입니다.
    # 도대체 cls는 무엇일까요?
    # 보편적으로 cls는 클래스와 메서드가 서로 참조하기 위해 사용하는 내부 인자입니다.
    # self랑은 무슨 관계지? 라는 생각이 보편적으로 들 수 있습니다.
    # self는 초기화가 끝나야지만 사용가능
    # __new__()를 진행하는 과정에서 아직 객체화가 완료되지 않았습니다.
    # 그렇기 때문에 self를 사용할 수 없는데
    # 이 시점에 클래스 자체에 접근 할 수 있는 인자가 바로 cls입니다.
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerlist = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝

    def match(self, playerId, nickname):
        player = Player()
        player.setPlayerId(playerId)
        player.setPlayerNickname(nickname)
        self.__playerlist.append(player)

    def getNickname(self, playerId):
        return [player.getPlayerNickname() for player in self.__playerlist if player.getPlayerId() == playerId]

    def getPlayerId(self, playerId):
        for player in self.__playerlist:
            if player.getPlayerId() == playerId:
                return player.getPlayerId()

        return None