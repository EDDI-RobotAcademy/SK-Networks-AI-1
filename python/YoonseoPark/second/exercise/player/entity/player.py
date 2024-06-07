class Player:
    __playerId = 0
    __autoIncrementPlayerId = 0
    def __init__(self, nickname):
        Player.__autoIncrementPlayerId += 1
        self.__playerId = Player.__autoIncrementPlayerId
        self.__nickname = nickname

    # entity에는 getter와 setter로만 구성해준다 생각해도 좋다.
    # 그러나 setter를 사용할 때는 정말 setter가 필요한지 고려해보고 사용해야 한다.
    def getPlayerId(self):
        return self.__playerId

    def getPlayerNickname(self):
        return self.__nickname