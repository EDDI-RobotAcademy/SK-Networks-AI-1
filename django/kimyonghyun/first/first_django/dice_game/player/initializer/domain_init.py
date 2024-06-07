from player.service.player_service_impl import PlayerServiceImpl

# 코드 작성하면서 대문자 소문자 이슈가 있었음
class DomainInitializer:
    @staticmethod
    def initPlayerDomain():
        PlayerServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()
