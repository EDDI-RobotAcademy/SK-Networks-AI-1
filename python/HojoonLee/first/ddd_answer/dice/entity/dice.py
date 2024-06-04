# entity 부분은 내가 어떤 서비스를 할거냐에 따라 구현이 달라진다.
class Dice:
    def __init__(self):
        # 변수에 __ 2개를 붙이는 이유 ? : 언더바 2개는 접근 제한자의 역할로 private를 의미합니다.
        # 그러므로 외부에서 '__'가 있는 정보를 함부로 수정할 수 없습니다.
        # 접근 제한자는 보안의 관점 보단 협력 시 기존 방식을 고수했는데(legacy), 이 스타일을 바꾸면 안되기 때문
        # 실제로 '__' 로 걸려 있는 값을 바꾸면 컴파일 에러가 발생함
        self.__diceNumber = 0
        self.__playerId = None # 누군가 굴렸기 때문에, 유저정보가 필요 (특히나 고유한 id로)

    def setDiceNumber(self, number):
        self.__diceNumber = number

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getDiceNumber(self):
        return self.__diceNumber

    def getPlayerId(self):
        return self.__playerId

# dice = Dice()
# dice.__diceNumber = 3
# print(dice.__diceNumber)
