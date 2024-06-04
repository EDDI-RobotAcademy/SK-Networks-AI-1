from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


class DomainInitializer:
    # @staticmethod가 붙어 있는 함수는 객체 생성 없이 사용 할 수 있는 함수입니다.
    @staticmethod
    def initDiceDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청 되는 것들은 기존에 만들어진 것을 반환함 (싱글톤 특성)
        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
