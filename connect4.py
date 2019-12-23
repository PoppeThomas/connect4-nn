# Run this file to play a game against the strategy determined below.
import sys
import pygame

from game.Game import Game
from learning.NNStrategy import NNStrategy

STRATEGY = NNStrategy()
STRATEGY.load_model()
GAME = Game(True, STRATEGY, None)
GAME.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            GAME.play(mouse_pos)

