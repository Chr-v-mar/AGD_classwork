class GameObj:
    def __init__(self,name,pos,solid):
        self.name = name
        self.pos = pos
        self.solid = solid

    #def __str__(self):


    def is_solid(self):
        return self.solid

class Character(GameObj):
    def __init__(self,name,pos,solid):
        self.name = name
        self.pos = pos

    def move(self,direction,value):
        future = self.find_next_location(direction,value)
        if self.future.is_solid():
            self.solid = future

        return self.pos

    def find_next_location(self,direction,value):
        future_pos = self.pos[direction] + 1
        return future_pos


