from Player.repository.player_repository_impl import PlayerRepositoryImpl
from initializer.domain_initializer import DomainInitializer

DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerId = 2
    firstnickname = "dd"

    playerRepository = PlayerRepositoryImpl.getInstance()
    playerRepository.match(firstPlayerId,firstnickname)


    firstPlayer = playerRepository.getplayerid(firstPlayerId)

    print(f"플레이어 아이디: {firstPlayer.getPlayerId()}")
    # print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")