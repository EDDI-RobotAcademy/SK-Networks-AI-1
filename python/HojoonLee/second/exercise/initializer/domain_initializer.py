from player.repository.player_repository_impl import PlayerRepositoryImpl


class DomainInitializer:
    # initializer : 각 도메인의 싱글톤을 만들어 주는 역할 >> 그래서 staticmethod를 써야함
    # @staticmethod가 있다면, 객체 생성 안해도 해당 변수를 쓸 수 있음
    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()



    @staticmethod
    def initEachDomain():
        # 여러 도메인을 사용할 때 각 도메인 마다의 기능을 위해 초기화 시켜줌
        # product 도메인 따로, account 도메인 따로 초기화..
        DomainInitializer.initPlayerDomain()  # player 도메인 추가