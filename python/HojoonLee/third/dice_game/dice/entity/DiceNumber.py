from enum import Enum # 열거형 만들기
# dice라는 entity를 표현하기 위해 entity 폴더에서 구현
class DiceNumber(Enum):
    # 각각의 문자들이 숫자로 대응
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
