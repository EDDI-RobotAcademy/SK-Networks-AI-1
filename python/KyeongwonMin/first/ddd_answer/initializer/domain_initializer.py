from dice.repository.dice_repository_Impl import DiceRepositoryImpl


class DomainInitializer:
    # @staticmethod 가 붙어 있는 녀석들은 객체 생성 없이 사용할 수 있는 함수입니다.
    @staticmethod
    def initDiceDomain():
        # 이부분에서 기존에 만들어진 부분을 받아옴
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청되는 것들은 기존에 만들어진것을 반환함(싱글톤 특성)
        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()