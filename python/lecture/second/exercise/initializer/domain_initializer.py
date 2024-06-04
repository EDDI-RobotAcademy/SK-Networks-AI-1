from player.service.player_service_impl import PlayerServiceImpl


class DomainInitializer:
    @staticmethod
    def initPlayerDomain():
        PlayerServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()
