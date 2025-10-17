from random import randint
from symtable import Class

import class_exercises


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




    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self, dead:bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)


    def return_character_status(self):
        return f'{self.name} has {self.skill} skill and {self.stamina} stamina'

    def return_roll_status(self):
        return f'{self.name} has rolled a {self.roll} roll for a total score of {self.score}'

    def find_score(self,roll,score):
        self.roll = dice_sum(2)
        self.score = self.roll +self.skill
        return self.score

    def take_hit(self, damage=2):
        self.stamina -= damage

    def fight_round(self, other):
        self.find_score()
        other.find_score()
        if self.score > other.score:
            other.take_hit()
            result = 'Win'
        elif other.score > self.score:
            self.take_hit()
            result = 'Loss'
        else:
            self.take_hit()
            other.take_hit()
            result = 'Draw'
        return result


class PlayerCharacter(Character):
    def __init__(self,name,skill, stamina,luck):
        super().__init__(name,skill,stamina)
        self.luck = luck

    @classmethod
    def generate_player_character(cls,name):
        skill = 6 + dice_sum(1,6)
        stamina = 12 + dice_sum(2,6)
        luck = 6 + dice_sum(1,6)
        return cls(name,skill,stamina,luck)

pc = Character('Dm',2,15)
orc = Character('Orc',2,10)