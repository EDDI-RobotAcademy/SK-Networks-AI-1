from player.service.player_service_impl import PlayerServiceImpl


class DomainInitializer:
    # @staticmethod가 붙어 있는 녀석들을 객체 생성 없이 사용할 수 있는 함수입니다.
    @staticmethod
    def initPlayerDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴.
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청되는 것들은 기존에 만들어진 것을 반환함(singleton 특성)
        PlayerServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()
