from random import randint, choice
import time
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
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def __str__(self):
        return f'{self.name}'

    #def return_character_status(self):
        #return f"{self.player.name} has skill {self.player.skill} skill and {self.player.stamina} stamina"

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
        return f'{self.name} has skill {self.skill} and stamina {self.stamina}'

    def return_roll_status(self):
        return f'{self.name} rolled {self.roll} for a total score of {self.score}'

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
            result = 'won'
        elif other.score > self.score:
            self.take_hit()
            result = 'lost'
        else:
            self.take_hit()
            other.take_hit()
            result = 'draw'
        return result


class PlayerCharacter(Character):
    def __init__(self,name,skill, stamina,luck):
        super().__init__(name,skill,stamina)
        self.luck = luck

    def __repr__(self):
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    @classmethod
    def generate_player_character(cls,name):
        skill = 6 + dice_sum(1,6)
        stamina = 12 + dice_sum(2,6)
        luck = 6 + dice_sum(1,6)
        return cls(name,skill,stamina,luck)

    def test_luck(self):
        roll = dice_sum(2)
        if roll > self.luck:
            self.luck -= 1
            return False
        else:
            self.luck -= 1
            return True


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
        self.opponent = choice(self.creatures)
        self.creatures.remove(self.opponent)

    def set_player(self,player_character):
        self.player = player_character

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def return_round_result(self):
        msg =  (self.player.return_roll_status() + "\n" +
                self.opponent.return_character_status())
        if self.round_result == 'won':
            msg += "Player won this round\n"
        elif self.round_result == 'lost':
            msg += "Player lost this round\n"
        elif self.round_result == 'draw':
            msg += "This round was a draw\n"
        return msg


class GameCLI:
    def __init__(self):
        self.game = Game()
        self.run_game()

    def run_game(self):
        print("Welcome to Fighting Fantasy!")
        time.sleep(0.5)
        player_name = input("Enter a name to begin creating your character!: ")
        self.game.set_player(PlayerCharacter.generate_player_character(player_name))
        time.sleep(0.5)
        print(f'Welcome {player_name}')
        print(self.game.player.return_character_status())
        self.fight_opponent()

    def fight_opponent(self):
        self.game.choose_opponent()
        time.sleep(0.5)
        print(f'You will be fighting {self.game.opponent}')
        print(self.game.opponent.return_character_status() + '\n')
        self.fight_battle()

    def fight_battle(self):
        continue_battle = True
        while continue_battle:
            print(self.game.return_round_result())
            print()
            action = input("Would you like to fight a round (y/n)? ").strip().lower()
            if action == 'n':
                print("You flee in terror!")
                continue_battle = False
            else:
                self.game.resolve_fight_round()
                print(self.game.return_round_result())
            if self.game.player.is_dead:
                print('You died')
                continue_battle = False
            if self.game.opponent.is_dead:
                print(f"You defeated the {self.game.opponent.name}")
                continue_battle = False


if __name__ == "__main__":
    GameCLI()


#Hero = PlayerCharacter.generate_player_character('Chris')
#Evep = Character('EvilEep',2,15)
#Orc = Character('Orc',2,10)