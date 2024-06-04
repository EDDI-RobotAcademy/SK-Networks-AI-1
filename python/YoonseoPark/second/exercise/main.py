from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

DomainInitializer.initEachDomain()

# 조건은 아래와 같습니다.
# Player는 고유 번호 (playerId)
# 그리고 닉네임 (nickname)을 가지고 있습니다.

# 2명 정도의 Player를 만들고
# playerId를 통해 nickname을 출력하도록 만들어봅시다!

if __name__ == "__main__":

    firstPlayerNickname = "1번 사용자"

    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번 사용자"
    playerService.createPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f"firstPlayer id: {firstPlayer.getPlayerId()}")
    print(f"firstPlayer nickname: {firstPlayer.getPlayerNickname()}")

    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f"secondPlayer id: {secondPlayer.getPlayerId()}")
    print(f"secondPlayer nickname: {secondPlayer.getPlayerNickname()}")