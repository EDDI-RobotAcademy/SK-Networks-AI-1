class Player:
    def __init__(self):
        self.__playerId = 0
        self.__nickname = None
    def setNickname(self, name):
        self.__nickname = name

    def getNickname(self):
        return self.__nickname

    def getPlayerId(self):
        return self.__playerId

    def setPlayerId(self, number):
        self.__playerId = number

if __name__ == '__main__':
    p1 = Player()
    p1.setNickname('minn')
    p1.setPlayerId(1)