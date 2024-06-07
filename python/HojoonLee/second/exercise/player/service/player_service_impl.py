from player.repository.player_repository_impl import PlayerRepositoryImpl
from player.service.player_service import PlayerService

class PlayerServiceImpl(PlayerService):

    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # service -> repository 순서로 접근하는데,
            # repository도 싱글톤 방식으로 한번만 잡아주도록 한다.
            # 이렇게 해도 되긴 함 근데 __을 통해 관례적으로 바꾸지 않는다 명시
            # cls.__instance.playerRepository = PlayerRepositoryImpl.getInstance()

            # 여기의 __playerRepository는 실제 있던 멤버변수는 아니고 내가 지어준 이름
            # PlayerRepositoryImpl의 객체를 받을거라 명시적으로 이름지음
            # cls.__instance는 현재 PlayerService
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None: # 해당 객체가 없다면
            cls.__instance = cls() # 불러온 객체(cls)로 할당
        return cls.__instance
    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝!

    # 무조건 repo로 감싼다? (순서상 service먼저 호출되고 그다음 여기서 repo를 부르므로..)
    def createPlayer(self, nickname):
        self.__playerRepository.create(nickname)
        # 위에서처럼 playerRepository로 instance를 만들고
        # self.playerRepository.create(nickname)을 해도 가능함 근데, __를 통해 바꾸지 않는다 약속

    def findPlayerByNickname(self, nickname):
        return self.__playerRepository.findPlayerByNickname(nickname)