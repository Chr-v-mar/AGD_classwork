from random import randint, choice
import random


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

    def find_score(self):
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

class Game:
    @classmethod
    def load_creatures(cls):
        creatures = [Character("Dragon",10,22),
                     Character("Orc",7,10),
                     Character("Snake",3,10),
                     Character("Skeleton",5,8),
                     Character("King Rat",5,5),
                     Character("Dark Knight",10,12),
                     ]
        return creatures
    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.opponent = random.choice(self.creatures)
        self.creatures.remove(self.opponent)

    def set_player(self,player_character):
        self.player = player_character

Hero = PlayerCharacter.generate_player_character('Chris')
Evep = Character('EvilEep',2,15)
Orc = Character('Orc',2,10)