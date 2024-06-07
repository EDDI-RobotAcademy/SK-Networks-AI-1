from initializer.domain_initializer import DomainInitializer

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()

if __name__ = "__main__":
    firstPlayerNickname = "1번 사용자"

    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer(firstPlayerNickname)

    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    print(f"firstPlayer: {firstPlayer}")