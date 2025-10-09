from random import randint
from symtable import Class

#def dice_sum(num_dice,sides):
    #total = sum(randint(1,sides) for roll in range (num_dice)) - alternative dice rolling system
    #return total
#print(dice_sum(1,8))

def dice_sum(num_dice: int = 1, num_sides: int = 6):
    return sum(randint(1, num_sides) for _ in range(num_dice))


class Character():
    def __init__(self, name, skill, stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', Skill = '{self.skill}', Stamina = '{self.stamina}')"

    def find_score(self,roll,score):

