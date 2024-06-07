from player.repository.player_repository_impl import PlayerRepositoryImpl
from initializer.domain_initializer import DomainInitializer

DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayer = {"playerId": "pid1", "nickname": "apple"}
    secondPlayer = {"playerId": "pid2", "nickname": "banana"}

    playerRepository = PlayerRepositoryImpl.getInstance()
    playerRepository.initPlayer(playerId=firstPlayer['playerId'], nickname=firstPlayer['nickname'])
    playerRepository.initPlayer(playerId=secondPlayer['playerId'], nickname=secondPlayer['nickname'])


    inputId = "pid1"
    playerChecker = playerRepository.checkPlayer(inputId)

    # 1인경우에 체크하고 없다면 None이 반환 -> 예외처리?
    if playerChecker:
        print(f"{inputId}의 nickname: {playerChecker.getNickname()}")

    inputId = "pid2"
    playerChecker = playerRepository.checkPlayer(inputId)

    if playerChecker:
        print(f"{inputId}의 nickname: {playerChecker.getNickname()}")

