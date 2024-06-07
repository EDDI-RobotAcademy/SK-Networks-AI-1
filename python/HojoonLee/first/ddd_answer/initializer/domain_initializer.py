from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


class DomainInitializer:
    # initializer : 각 도메인의 싱글톤을 만들어 주는 역할 >> 그래서 staticmethod를 써야함
    # @staticmethod가 있다면, 객체 생성 안해도 해당 변수를 쓸 수 있음
    @staticmethod
    def initDiceDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청 되는 것들은 기존에 만들어진 것을 반환함 (싱글톤 특성)
        DiceRepositoryImpl.getInstance() # 객체 탐색해서 있다면 return instance
        # 앞으로 repo의 instance가 필요하다면, repoimpl에서 구현한 get 기능 가져오기
    
    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()
        
    @staticmethod
    def initEachDomain():
        # 여러 도메인을 사용할 때 각 도메인 마다의 기능을 위해 초기화 시켜줌
        # product 도메인 따로, account 도메인 따로 초기화..
        DomainInitializer.initDiceDomain()
        DomainInitializer.initPlayerDomain() # player 도메인 추가
    
