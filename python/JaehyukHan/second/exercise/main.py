"""
main에서는 Service 패키지만 접근함으로써, 코드의 가독성을 높이고
사용자가 Service에서 참조하고 있는 Repository나
그 이면에 있는 Entity에 접근하여 생길 수 있는 문제를 사전에 예방할 수 있음

Singleton
> player class에서 __playerList를 통해 player 정보들을 계속 관리하고 있는데,
> Singleton 방식이 아닌 다른 방식으로 구현하게 되면 객체가 생성될 때마다 관리하던 player들의 정보가 사라지게됨
> 그 정보를 계속 유지하기 위해 getInstance로 객체를 재활용하는 것
"""

from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

DomainInitializer.initEachDomain()

# 조건은 아래와 같습니다.
# Player는 고유 번호(playerId)
# 그리고 닉네임 (nickname) 을 가지고 있습니다.

# 2명 정도의 Player를 만들고
# playerId를 통해 nickname을 출력하도록 만들어봅시다!

if __name__ == "__main__":
    firstPlayerNickname = "1번사용자"

    # 아래 코드에서 딱 한번엔 Player instance를 생성함
    playerService = PlayerServiceImpl.getInstance()

    # 이 아래로는 별도의 instance를 생성하는 것이 아니라,
    # 위에서 한번 만들어놓은 instance를 재활용해서 사용함
    playerService.createPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번사용자"
    playerService.createPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f"firstPlayer id: {firstPlayer.getPlayerId()}")
    print(f"firstPlayer nickname: {firstPlayer.getPlayerNickname()}")

    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f"firstPlayer id: {secondPlayer.getPlayerId()}")
    print(f"firstPlayer nickname: {secondPlayer.getPlayerNickname()}")
