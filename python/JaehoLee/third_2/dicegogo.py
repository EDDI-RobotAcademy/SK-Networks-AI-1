# PlayerRepository 클래스에 싱글톤 패턴을 적용한다.

# Player 클래스 정의 플레이어의 정보를 받는다.
class Player:
    def __init__(self,player_id,nickname):
        self.player_id = player_id
        self.nickname = nickname
    def roll_dice(self, dice):
        return dice.roll()# 아직 .roll()메서드는 안만들어졌다

#Dice 클래스 정의 roll이 실행되는 부분
class Dice:
    def roll(self):
        import random
        return random.randint(1,6) # 주사위 숫자 변경가능성에 대한 대비가 없다 (고정값을넣음)

# PlayerRepository 클래스 정의
class PlayerRepository:
    _instance = None

    def __new__(cls, *args, **kwargs): # *args는 튜플형태, **kwargs는 딕셔너리형태로전달됨 -> 메서드를유연하게한다
        if cls._instance is None:
            cls._instance = super(PlayerRepository, cls).__new__(cls)
            cls._instance.players = {}
        return cls._instance
        # PR클래스선언,
        # 클래스변수로 _instance 변수를 생성했고  None값을 할당
        # PlayerRepository선언시 가장먼저 __new__메서드가 해석됨
        # PlayerRepository.instance가 None이면:
        # _instance에 클래스 자체를 할당 (__new__라는 특수메서드이용)(2개 매개변수사용해서 현재클래스로특정했고
        # 접근한 object클래스에서 __new__(cls)메서드를 사용해 cls._instance에 인스턴스를 할당
        # 그리고 players라는 속성을 추가하고 빈 딕셔너리를 할당
        # None이 아니라면 그것을 return
        # 간단하게는 호출될때 새로운 인스턴스가 생기지않고 처음 호출때 사용된 인스턴스를
        # __new__를통해 고정하는것
    def add(self, player):
            self.players[player.player_id] = player

        # add메서드선언 (player인자받음) 딕셔너리에 호출하는객체속성의player_id를 키, 받은인자를 value로대입
    def get(self, player_id):
            return self.players.get(player_id)
        # 딕셔너리의 get함수이용해서 키값에맞는 value반환 ~~ 하나의 객체로 고정되었기때문에
        #                                            딕셔너리에 계속 추가된다
class DiceGame:
    def __init__(self, player_repository): #객체와 인자를받음
        self.player_repository = player_repository #받은인자를 속성에추가
        self.dice = Dice() # 객체에 dice속성을 추가하고 선언한 Dice()클래스대입
    def play_game(self, player1_id, player2_id):
        player1 = self.player_repository.get(player1_id) # init으로생긴속성에대해 get을실행하게함
        player2 = self.player_repository.get(player2_id) # repo에서가져온 것에해당하는player_id의 객체를가져옴

        score1 = player1.roll_dice(self.dice)
        score2 = player2.roll_dice(self.dice)

        print(f'{player1.nickname}의 숫자 {score1}')
        print(f'{player2.nickname}의 숫자 {score2}')

        if score1 > score2:
            return f'{player1.nickname} 승리'
        if score2> score1:
            return f'{player2.nickname} 승리'
        return '무승부입니다'

player1 = Player(1, "부처")
player2 = Player(2, "예수")

# PlayerRepository 객체 생성 (싱글톤)
player_repository = PlayerRepository()

# Player 객체 추가
player_repository.add(player1)
player_repository.add(player2)

# DiceGame 객체 생성
game = DiceGame(player_repository)

# 주사위 게임 실행 및 승자 출력
result = game.play_game(1, 2)
print(result)




