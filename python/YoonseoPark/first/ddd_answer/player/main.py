from initializer.domain_initializer import DomainInitializer
from player.repository.player_repository_impl import PlayerRepositoryImpl

DomainInitializer.initEachDomain()  # Domain 객체들을 초기화

if __name__ == "__main__":

    playerRepository = PlayerRepositoryImpl.getInstance()

    playerRepository.registerPlayer(1, "홍길동")
    playerRepository.registerPlayer(2, "김길동")

    firstPlayer = playerRepository.getNickname(1)
    secondPlayer = playerRepository.getNickname(2)

    print(f"첫 번째 플레이어: {firstPlayer}")
    print(f"두 번째 플레이어: {secondPlayer}")