class Gameobj:
    def __str__(self,name,pos,solid):
        self.name = name
        self.pos = pos
        self.solid = solid

    def is_solid(self):
        return self.solid

class Character(Gameobj):
    def __init__(self,name,pos,solid):
        self.name = name
        self.pos = pos

    def move(self,direction,value):
        self.pos = self.find_next_location(direction,value)
        return self.pos

    def find_next_location(self,direction,value):
        future_pos = self.pos[direction] + 1
        return future_pos

class Game:
    def set_up(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = ()
        self.start = ()
        self.exit = ()

    def add_background(self,btype,pos):
        self.backgrounds[pos[0]][pos[1]] = btype

    def set_background_from_file(self,filename):
        with open(filename,'r') as my_file:
            data = my_file.readlines()
            for line in data:
                line = line.strip()
                line = line.split()


