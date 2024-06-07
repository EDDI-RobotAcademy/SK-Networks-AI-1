from player.service.player_service_impl import PlayerServiceImpl
from game.service.game_service_impl import GameServiceImpl

from initializer.domain_initializer import DomainInitializer

DomainInitializer.initEachDomain()


if __name__ == "__main__":
    playerService = PlayerServiceImpl.getInstance()

    firstPlayerNickname = "One"
    playerService.createPlayer(firstPlayerNickname)
    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)

    secondPlayerNickname = "Two"
    playerService.createPlayer(secondPlayerNickname)
    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)

    gameService = GameServiceImpl.getInstance()
    gameService.playGame(firstPlayer, secondPlayer)

    winner = gameService.findWinner(firstPlayer, secondPlayer)

    if winner is None:
        print("DRAW!")

    else:
        print(f"Winner is {winner.getPlayerId()}")
