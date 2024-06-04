from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

DomainInitializer.initEachDomain()  # Domain 객체들을 초기화

if __name__ == "__main__":
    firstPlayerNickname = "1번사용자"

    playerService = PlayerServiceImpl.getInstance()
    playerService.registerPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번사용자"
    playerService.registerPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f"firstPlayer id: {firstPlayer.getPlayerId()}")
    print(f"firstPlayer nickname: {firstPlayer.getPlayerNickname()}")

    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f"secondPlayer id: {secondPlayer.getPlayerId()}")
    print(f"secondPlayer nickname: {secondPlayer.getPlayerNickname()}")