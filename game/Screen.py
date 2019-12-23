import pygame
import os

from game.Constants import HUMAN, NB_COLUMNS, NB_ROWS


pygame.init()
COL_WIDTH = 70
ROW_HEIGHT = COL_WIDTH
SCREEN_WIDTH = NB_COLUMNS * COL_WIDTH
SCREEN_HEIGHT = NB_ROWS * ROW_HEIGHT
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
IMG_RED = pygame.image.load(os.path.join('img', "red.png")).convert()
IMG_YELLOW = pygame.image.load(os.path.join('img', "yellow.png")).convert()
IMG_EMPTY = pygame.image.load(os.path.join('img', "empty.png")).convert()
FONT = pygame.font.Font(None, 100)


# All display logic (using pygame) is bundled in this class.  The game class drives the screen.
class Screen:

    def __init__(self):
        pass

    @staticmethod
    def __draw(image, row, col):
        SCREEN.blit(image, (col * COL_WIDTH, (NB_ROWS - row - 1) * ROW_HEIGHT))

    def draw_empty(self):
        pygame.display.set_caption("Connect 4")
        for col in range(NB_COLUMNS):
            for row in range(NB_ROWS):
                self.__draw(IMG_EMPTY, row, col)
        pygame.display.flip()

    @staticmethod
    def get_column(coordinate):
        col = int(coordinate[0] / COL_WIDTH)
        pos_in_col = coordinate[0] % COL_WIDTH
        margin = 8
        if (pos_in_col < margin) | (pos_in_col > (COL_WIDTH - margin)):
            return -1
        return col

    def play(self, turn, row, col):
        image = IMG_YELLOW if (turn == HUMAN) else IMG_RED
        self.__draw(image, row, col)
        pygame.display.flip()

    def display_win(self, turn):
        text_surface = FONT.render(("Yellow" if (turn == HUMAN) else "Red") + " wins!", True, (255, 255, 255))
        self.__draw_text(text_surface)

    def display_tie(self):
        text_surface = FONT.render("Tie!", True, (255, 255, 255))
        self.__draw_text(text_surface)

    @staticmethod
    def __draw_text(text_surface):
        width = text_surface.get_width()
        height = text_surface.get_height()
        text_pos = ((SCREEN_WIDTH - width) / 2, (SCREEN_HEIGHT - height) / 2)
        SCREEN.blit(text_surface, text_pos)
        pygame.display.flip()

