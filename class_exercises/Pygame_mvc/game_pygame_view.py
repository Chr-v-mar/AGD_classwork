import pygame
from game_controller import Game
import keyboard


from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SQUARE_SIZE = 50

BACKGROUND_COLORS = {'W': 'gray30',
                     'S': 'gold',
                     'E': 'dodgerblue',
                     'F': 'white'
                     }
PLAYER_COLOR = 'firebrick'

class GameGUI:
    key_moves = {K_UP: 'w',
                 K_DOWN: 's',
                 K_RIGHT: 'a',
                 K_LEFT: 'd',
                 }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')

        # Set clock so that FPS can be limited
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.move_direction: str | None = None

        self.screen = pygame.display.set_mode([self.game.dimensions[1] * SQUARE_SIZE,
                                               self.game.dimensions[0] * SQUARE_SIZE])
        self.running = True

    @staticmethod
    def _convert_position(pos: tuple, center: bool = False) -> tuple[int, int]:
        x, y = pos[1]*SQUARE_SIZE, pos[0]*SQUARE_SIZE
        return x,y
        """ Convert a grid position in the game to an (x, y) coordinate"""
        """if centre is false the position returned is top-left and if center is true"""
        """the position returned is the centre """


    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60) # cap to 60 FPS
        pygame.quit()

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None
            # elif (event.type == KEYDOWN or event.type == K_LEFT or event.type == K_RIGHT or event.type == K_UP):
            if event.type == KEYDOWN and event.key in self.key_moves:
                self.move_direction = self.key_moves[event.key]

            else:
                self.move_direction = None


    def _process_game_logic(self):
        """ Implements character moves and checks if player has reached the exit """
        for character in self.game.characters:
            move = self.game.move_character(character, self.move_direction)

    def _draw(self):
        """draw background first then characters"""
        self._draw_background()
        self._draw_characters()
        pygame.display.flip()

    def _draw_background(self):
        """Loop through all the game backgrounds and draw a rectangle of the appropriate colour"""
        self.screen.fill(BACKGROUND_COLORS['F'])
        for bg in self.game.background:
            grid_x, grid_y = self._convert_position(bg.pos)
            color = BACKGROUND_COLORS[bg.name]
            pygame.draw.rect(self.screen, color, (grid_x, grid_y, SQUARE_SIZE, SQUARE_SIZE))

    def _draw_characters(self):
        """Loop through the characters and draw a circle for each character"""
        for character in self.game.characters:
            grid_x, grid_y = self._convert_position(character.pos)
            color = PLAYER_COLOR
            pygame.draw.circle(self.screen, color, (grid_x+(SQUARE_SIZE*0.5), grid_y+(SQUARE_SIZE*0.5)), SQUARE_SIZE/4)

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()