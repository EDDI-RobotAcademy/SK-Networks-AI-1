from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()

# Top-down process
# 이런 기능이 있으면 좋겠어~ 정도의 느낌으로 main 먼저 작성.
# 선 기능 정의 -> 후 세부 기능
# 세부 사항에 종속되지 않도록 개발하는 것이 top-down

if __name__ == "__main__":
    firstPlayerNickname = "1번 사용자"

    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번 사용자"
    playerService.createPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f'firstPlayer id: {firstPlayer.getPlayerId()}')
    print(f'firstPlayer nickname: {firstPlayer.getPlayerNickname()}')

    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f'secondPlayer id: {secondPlayer.getPlayerId()}')
    print(f'secondPlayer nickname: {secondPlayer.getPlayerNickname()}')
