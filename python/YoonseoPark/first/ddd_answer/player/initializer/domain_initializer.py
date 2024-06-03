from player.repository.player_repository_impl import PlayerRepositoryImpl


class DomainInitializer:
    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()
