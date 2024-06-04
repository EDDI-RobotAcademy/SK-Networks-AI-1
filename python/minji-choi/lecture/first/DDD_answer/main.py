from Initializer.domain_initializer import DomainInitializer
from Player.repository.player_repository_impl import PlayerRepositoryImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl

DomainInitializer.initEachDomain()  # 클래스 불러오지 않아도 사용 가능

if __name__ == '__main__':
    firstPlayerId = 1

    # diceRepository = DiceRepositoryImpl.getInstance()
    # diceRepository.rollDice(firstPlayerId)
    # firstPlayerDice = diceRepository.checkDice(firstPlayerId)

    playerRepository = PlayerRepositoryImpl.getInstance()
    playerRepository.setPlayer(firstPlayerId, 'minnji')
    print(playerRepository.getNickname(firstPlayerId))
    firstPlayerNickname = playerRepository.checkPlayer(firstPlayerId)
    # print(f"첫번째 주사위 눈금 : {firstPlayerDice.getDiceNumber()}")
    # print(f"첫번째 주사위 굴린 player : {firstPlayerDice.getPlayerId()}")

    #
    print(f"첫번째 플레이어 닉네임 : {firstPlayerNickname.getNickname()}")
    print(f"첫번째 플레이어 고유번호 : {firstPlayerNickname.getPlayerId()}")