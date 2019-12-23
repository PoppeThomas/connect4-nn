import sys
import time
import pygame

from game.Constants import COMPUTER
from game.Game import Game


# let the given strategies play against each other, and show the moves on the board while playing
def simulate_game(computer_strategy, other_strategy):
    game = Game(True, computer_strategy, other_strategy)
    game.start()

    while True:
        if not game.board.finished:
            game.let_computer_play()
            time.sleep(0.5)
        else:
            time.sleep(2)
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


# play 100 matches and return the number of times strategy1 wins
# TODO count a tie as 0.5 win
def match_strategies(strategy1, strategy2):
    nb_wins = 0
    game = Game(False, strategy1, strategy2)
    for game_no in range(100):
        game.start()
        while not game.board.finished:
            game.let_computer_play()
        if game.turn == COMPUTER:
            nb_wins = nb_wins + 1
    return nb_wins
