from game_controller import Game
from game_objects import Character


class GameTUI:

    def __init__(self):
        self.game = Game()
        self.game.set_up()

        # spawn player at first empty tile
        self.player = Character("P", (0, 0), False)
        self.game.characters.append(self.player)

    def build_grid(self):
        grid = {}

        for obj in self.game.background:
            grid[obj.pos] = obj.name

        for char in self.game.characters:
            grid[char.pos] = char.name

        return grid

    def draw(self):
        grid = self.build_grid()

        max_row = max(pos[0] for pos in grid)
        max_col = max(pos[1] for pos in grid)

        print("\nGAME MAP\n")

        for r in range(max_row + 1):
            row = ""
            for c in range(max_col + 1):
                row += grid.get((r, c), ".") + " "
            print(row)

        print()

    def player_turn(self):
        command = input("Move (north/south/east/west) or quit (q): ").lower()

        if command == "q":
            return False

        self.player.move(self.game, command)

        return True

    def run(self):

        running = True

        while running:
            print("\n" * 5)
            self.draw()
            running = self.player_turn()


if __name__ == "__main__":
    tui = GameTUI()
    tui.run()