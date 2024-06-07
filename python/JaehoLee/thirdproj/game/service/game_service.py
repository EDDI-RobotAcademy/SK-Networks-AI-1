from dice.entity.dice import Dice
from player.repository.player_repository import PlayerRepository

class GameService:
    def __init__(self,player_repository):
        self.player_repository = player_repository
        self.dice = Dice()

    def play_game(self, player1_id, player2_id):
        player1 = self.player_repository.get(player1_id)
        player2 = self.player_repository.get(player2_id)

        score1 = player1.roll_dice(self.dice)
        score2 = player2.roll_dice(self.dice)

        print(f'{player1.nickname} 이(가) {score1} 굴렸음')
        print(f'{player2.nickname} 이(가) {score2} 굴렸음')


        if score1 > score2:
            return f'{player1.nickname} 승리 ㅋㅋ'
        if score2 > score1:
            return f'{player2.nickname} 승리 ㅋㅋ'

        return '무승부입니다.'

