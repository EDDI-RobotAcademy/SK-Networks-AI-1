from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerNickname = "1번사용자"

    # 최상위 agenda를 정의 (세부사항 x)
    # controller -> service -> repository -> entity
    # 아직 controller 구현을 안해서 현재 최상위는 service이므로 main에서는 service를 통해 정의
    PlayerService = PlayerServiceImpl.getInstance() # service로 우회해서 객체 생성할게
    PlayerService.createPlayer(firstPlayerNickname) # service의 createPlayer 기능

    # agneda는 만들었으니, 제대로 됐나 한번 확인 해보자
    # 여기서 firstPlayer는 인터페이스 방식으로 불러오기 때문에 파급을 최소화 시키도록 만듦 (service, repo)
    firstPlayer = PlayerService.findPlayerByNickname("1번사용자")
    print(f"firstPlayer: {firstPlayer.getPlayerId()}") # player정보를 확인 (firstPlayer는 class ?)
    print(f"firstPlayer nickname: {firstPlayer.getPlayerNickname()}")

    # 세부사항(entity)은 가장 마지막에 결정한다. Entity == (Player 정보)