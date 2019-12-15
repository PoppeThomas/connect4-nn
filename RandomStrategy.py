import random


class RandomStrategy:

    def __init__(self):
        pass

    def next_move(self, legal_moves):
        return random.choice(legal_moves)