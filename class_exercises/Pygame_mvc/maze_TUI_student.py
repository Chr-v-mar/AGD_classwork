from game_controller import Game


class TextInterface:
    """ Create a text-based interface for the turn-based game."""

    def __init__(self):
        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True

    def _create_area(self):
        """Create a list of lists representing the map."""

        max_row = max(obj.pos[0] for obj in self.game.background)
        max_col = max(obj.pos[1] for obj in self.game.background)
        self.game_area = [["." for _ in range(max_col + 1)] for _ in range(max_row + 1)]


        for obj in self.game.background:
            r, c = obj.pos
            self.game_area[r][c] = obj.name[0]

        for char in self.game.characters:
            r, c = char.pos
            self.game_area[r][c] = char.name[0]

    def _draw_area(self):
        """Draw the grid with borders and wall symbols."""

        self._create_area()
        rows = len(self.game_area)
        cols = len(self.game_area[0])
        print("┌" + "─" * (cols * 2) + "┐")

        for row in self.game_area:
            line = "│"
            for cell in row:
                if cell == "W":
                    cell = "\u2593"
                line += cell + " "
            line += "│"
            print(line)

        print("└" + "─" * (cols * 2) + "┘")

    def _handle_input(self):
        """Handle player movement input."""

        direction = input("Move (north/south/east/west) or Q: ").lower()

        if direction == "q":
            self.running = False
            return

        new_pos = self.player.find_next_move(direction)

        if new_pos:
            self.game.move_character(self.player, new_pos)

    def main_loop(self):
        """Keep drawing the area and asking for player moves while running."""


        while self.running:
            self._draw_area()
            self._handle_input()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()

