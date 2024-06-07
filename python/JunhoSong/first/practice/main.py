import random

class Dice:
    def rollDice(self):
        return random.randint(1, 6)

dice = Dice()
dice_number = dice.rollDice()

print("주사위숫자:", dice_number)