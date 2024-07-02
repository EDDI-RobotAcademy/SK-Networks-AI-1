class Player:
    def __init__(self, player_id, nickname):
        self.player_id = player_id
        self.nickname = nickname

class PlayerRepository:
    def __init__(self):
        self.players = {}

    def add(self, player):
        self.players[player.player_id] = player

    def get(self, player_id):
        return self.players.get(player_id)

# Player 객체 생성
user1 = Player('11', 'zz')

# PlayerRepository 객체 생성
plrepo = PlayerRepository()

# Player 객체 추가
plrepo.add(user1)

# Player 객체 검색
retrieved_player = plrepo.get('11')

# 검색된 Player 객체의 속성 출력
if retrieved_player:
    print(f"Player ID '11': {retrieved_player.nickname}")  # 출력: Player ID '11': zz
else:
    print("Player not found")
