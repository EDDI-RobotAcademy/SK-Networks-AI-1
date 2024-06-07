class Player:
    __playerId = 0
    __autoIncrementPlayerId = 0
    def __init__(self, nickname):
        Player.__autoIncrementPlayerId += 1
        self.__playerId = Player.__autoIncrementPlayerId
        # 불필요한 set은 init부분에 넣어 줄여주자
        # 닉네임은 변경한다라는 agenda(전제)가 없으므로 굳이 set이 필요하지 않음 >> 객체부를때만 넣어주면 됨!
        self.__nickname = nickname
    # 불필요한 set은 다 init에 했으므로 get만 멤버함수로 구현
    def getPlayerId(self):
        return self.__playerId

    def getPlayerNickname(self):
        return self.__nickname