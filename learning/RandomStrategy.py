import random


# Play a random legal move.  Used for comparing the performance of other strategies.
# Initially I also used it to bootstrap learning, but the played games were so bad that immediately
# simulating games with the NNStrategy turned out to be better.
class RandomStrategy:

    def __init__(self):
        pass

    def next_move(self, player, board):
        legal_moves = board.get_legal_moves()
        return random.choice(legal_moves)
