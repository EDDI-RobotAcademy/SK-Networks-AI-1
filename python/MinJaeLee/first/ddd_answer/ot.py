# 1. IoC (Inversion of Control) 가 필요한 이유에 대해 기술하시오.

# IoC는 소프트웨어 디자인 원칙.. 객체의 생성과 의존성 관리를 직접 하지 않고 외부에서 관리하는 개념.
# 소프트웨어의 구조를 더 유연하고 확장 가능하게 만들어줌. 대규모시스템에서의 중요성은 매우 커짐

# 의존성 관리 용이
# 테스트 용이
# 유연성 향성
# 재사용성 증가
# 모듈화 개선
# 코드 가독성 및 유지보수성 향상
# 비즈니스 로직과 설정의 분리
# 설정 중앙화

# 2. python으로 IoC를 하려면 무엇을 해야 하는가 ?

# 간단한 프로젝트에서는 수동 의존성 주입
# 대규모 프로젝트에서는 injector나 dependency_injector와 같은 라이브러리 사용

# 3. OOP(객체지향) 프로그래밍을 수행함에 있어 언어가 중요한지 중요하지 않은지에 대해 기술해보세요.

# 언어별 장단점이 있기때문에 프로젝트의 요구사항에 맞는 언어를 선택하는것이 중요.
# 결론: 중요하지 않다

# 4. 주사위 클래스를 작성하세요.
import random


class Dice:

    # 5. 주사위를 굴리는 서비스 코드를 작성하세요.

    def r_dice(self):
        return random.randint(6)


# 6. 사용자 클래스를 작성하세요.
class user:
    def user_info(self):
        return [{'id': '990817'}, {'nick': 'Meue'}]


# 7. 사용자(게임 플레이어)가 주사위를 굴린다는 아젠다를 Domain 개념으로 표현하세요.

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self, dice):
        return dice.roll()


class Turn:
    def __init__(self, player, dice):
        self.player = player
        self.dice = dice

    def execute(self):
        result = self.player.roll_dice(self.dice)
        print(f"{self.player.name} rolled a {result}")
        return result


class Game:
    def __init__(self, players):
        self.players = players
        self.current_turn_index = 0

    def start(self):
        print("Game started!")
        while not self.is_game_over():
            current_player = self.players[self.current_turn_index]
            turn = Turn(current_player, Dice())
            turn.execute()
            self.current_turn_index = (self.current_turn_index + 1) % len(self.players)
        print("Game over!")

    def is_game_over(self):
        return self.current_turn_index >= 10


players = [Player("Alice"), Player("Bob")]
game = Game(players)
game.start()

# 8. TDD 적용을 고려하여 위의 내용들에 대한 테스트가 가능하도록 구성하세요.

# 테스트 주도 개발(TDD, Test-Driven Development)은 소프트웨어 개발 방법론으로,
# 코드를 작성하기 전에 테스트 코드를 먼저 작성하는 방식입니다.
# TDD의 주요 목표는 코드 품질을 높이고, 오류를 줄이며, 리팩토링을 쉽게 하는 것입니다.

# 테스트 작성: 먼저 실패할 수밖에 없는 테스트 코드를 작성합니다.
# 테스트 실패 확인: 테스트를 실행하여 실패하는지 확인합니다.
# 코드 작성: 테스트를 통과하기 위해 최소한의 코드를 작성합니다.
# 테스트 통과 확인: 테스트를 다시 실행하여 통과하는지 확인합니다.
# 리팩토링: 코드의 중복을 제거하고, 더 나은 구조로 리팩토링합니다.
# 반복: 새로운 기능이나 변경 사항이 있을 때마다 이 과정을 반복합니다.

# 9. 마지막으로 위의 구성을 갖추지 않은 상태에서 시스템과 비즈니스가 점점 커진다면 어떤 일이 발생하게 될 것인지 예측해봅시다.

# 시스템의 복잡성과 유지보수성을 크게 저하시키며, 개발 속도와 품질에도 부정적인 영향을 미칠 수 있음


# ------------------------------------------------------------------------------------------------
# * 임의의 비즈니스를 진행할 때 시장에 빠르게 들어가고

#    진입한 시장에서 SW가 어느정도 검증 되었다면

#    지속적으로 사용자들의 요구 사항 변경에 대응하여 유지보수성과 확장성을 가져가야 합니다.

#    위의 기법들은 모두 비즈니스 지속성과 속도(생산성), 빠른 고객 대응을 유지하는 비결입니다.

#

# * 프로그램을 작성할 때 단순히 그냥 돌아가도록만 만들었거나

#    혹은 그냥 문제 풀이라는 관점만 바라보았다면

#    이 문제를 풀면서 다시 한 번 자신을 되돌아보는 계기가 되었으면 좋겠습니다.