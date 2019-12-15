import sys
import pygame

from Game import Game


GAME = Game()
GAME.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            GAME.play(mouse_pos)

