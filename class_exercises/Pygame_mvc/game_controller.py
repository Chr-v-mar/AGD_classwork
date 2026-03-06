import csv
from game_objects import GameObj, Character


class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = None
        self.start = None
        self.exit = None

    def __repr__(self):
        return (f"self.characters: {self.characters}\n"
                f"self.backgrounds: {self.backgrounds}\n"
                f"self.dimensions: {self.dimensions}\n"
                f"self.start: {self.start}\n"
                f"self.exit: {self.exit}")

    def add_background(self,btype,pos,solid):
        self.backgrounds.append(GameObj(name=btype,pos=pos,solid=solid))
        self.backgrounds = sorted(self.backgrounds, key=lambda obj: obj.pos)

    def set_background_from_file(self,filename):
        with open(filename,mode= 'r') as my_file:
            csvFile = csv.reader(my_file, delimiter=',')
            for i,row in enumerate(csvFile):
                for j,obj in enumerate(row):
                    solid = obj == ("W")
                    self.add_background(obj,(i,j), solid)
