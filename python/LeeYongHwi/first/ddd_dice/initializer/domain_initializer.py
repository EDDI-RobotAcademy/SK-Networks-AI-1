from dice.repository.dice_repository_impl import DiceRepositoryImpl


class DomainInitializer:
    #
    @staticmethod
    def initDiceDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청되는 것들은 기존에 만들어진 것을 변환함(싱글톤 특성)
        DiceRepositoryImpl.getInstance()

    @staticmethod  # DomainInitializer가 생성되지 않아도 쓸 수 있게
    def initEachDomain():
        DomainInitializer.initDiceDomain()