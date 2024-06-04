class Player:
    __playerId = 0
    __autoIncrementPlayerId = 0

    def __init__(self, nickname):
        Player.__autoIncrementPlayerId += 1
        self.__playerId = Player.__autoIncrementPlayerId
        self.__nickname = nickname

    def getPlayerId(self):
        return self.__playerId

    def getPlayerNickname(self):
        return self.__nickname