from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from player.service.player_service_impl import PlayerServiceImpl

if __name__ == "__main__":

    # -------- 2명의 player 등록  --------
    playerService = PlayerServiceImpl.getInstance()

    firstPlayerNickname = "패트"
    playerService.registerPlayer(firstPlayerNickname)

    secondPlayerNickname = "매트"
    playerService.registerPlayer(secondPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)
    print(f"첫번째 사용자 => nickname: {firstPlayer.getPlayerNickname()}, id: {firstPlayer.getPlayerId()}")
    print(f"두번째 사용자 => nickname: {secondPlayer.getPlayerNickname()}, id: {secondPlayer.getPlayerId()}")

    # -------- 각 사용자 별 주사위 던지기 --------
    diceRepository = DiceRepositoryImpl.getInstance()

    diceRepository.rollDice(firstPlayer.getPlayerId())
    diceRepository.rollDice(secondPlayer.getPlayerId())

    firstPlayerDice = diceRepository.checkDice(firstPlayer.getPlayerId())
    secondPlayerDice = diceRepository.checkDice(secondPlayer.getPlayerId())
    print(f"{firstPlayerNickname} 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"{secondPlayerNickname} 주사위 눈금: {secondPlayerDice.getDiceNumber()}")

    # -------- dice --------
    # gameRepository = GameRepositoryImpl.getInstance()
    # gameRepository.makeGame(firstPlayer.getPlayerId(), secondPlayer.getPlayerId())
    # print(f"{}가 승리하였습니다.")

