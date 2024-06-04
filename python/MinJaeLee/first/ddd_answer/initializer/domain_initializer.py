from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player_domain.repository.playerdomain_repository_impl import PlayerDomain_Repo_Impl


class DomainInitializer:
    # @staticmethod가 붙어있는 놈들은 객체생성 없이 사용할 수 있는함수입니다
    @staticmethod
    def initDiceDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴
        # 만약 기존에 만들어진 것이 없다면, 새로 만들고
        # 이후 요청되는 것들은 기존에 만들어진 것을 반환함(싱글톤 특성)
        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerDomain_Repo_Impl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
