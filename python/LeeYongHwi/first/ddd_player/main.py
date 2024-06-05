from player.service.player_service_impl import PlayerServiceImpl
from initializer.domain_initializer import DomainInitializer

DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerNickname = "1번사용자"

    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번사용자"
    playerService.createPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f"firstPlayer id: {firstPlayer.getPlayerId()}")
    print(f"firstPlayer nickname: {firstPlayer.getPlayerNickname()}")

    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f"secondPlayer id: {secondPlayer.getPlayerId()}")
    print(f"secondPlayer nickname: {secondPlayer.getPlayerNickname()}")

