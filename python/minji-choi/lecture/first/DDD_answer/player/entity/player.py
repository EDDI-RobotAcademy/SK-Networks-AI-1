class Player:
    __playerId = 0
    __autoIncrementPlayerId = 0
    def __init__(self, nickname):
        Player.__autoIncrementPlayerId += 1
        self.__playerId = Player.__autoIncrementPlayerId
        self.__nickname = nickname

    def getNickname(self):
        return self.__nickname

    def getPlayerId(self):
        return self.__playerId

