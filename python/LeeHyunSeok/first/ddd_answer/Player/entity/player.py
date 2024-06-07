class Player:
    def __init__(self):
        self.__playernickname = None
        self.__playerId = None

    def setplayerid(self, playerId):
        self.__playerId = playerId


    def setplayernickname(self, playernickname):
        self.__playernickname = playernickname


    def getplayerid(self):
        return self.__playerId


    def getplayernickname(self):
        return self.__playernickname