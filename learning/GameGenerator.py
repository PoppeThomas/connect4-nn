import numpy as np

from game.Constants import NB_COLUMNS, NB_ROWS, COMPUTER
from game.Game import Game

MAX_SCORE = 1
SCORE_DECREASE_RATE = 0.9


# Generate a lot of games, feeding the results to the given learning strategy.
# The playing strategy of the 2 players can be either the learning strategy, but also another strategy if required.
def generate(nb_games, nb_games_per_learning_iteration, learning_strategy, playing_strategy1, playing_strategy2):
    game = Game(False, playing_strategy1, playing_strategy2)
    boards_with_score = np.empty((0, NB_ROWS * NB_COLUMNS + 1))
    for game_no in range(nb_games):
        boards_from_game = np.empty((0, NB_ROWS * NB_COLUMNS))
        game.start()
        if game.nb_moves > 0:
            # if a move has been made automatically, it was the computer that had to make the opening move
            # hence, we don't need the factor that's 4 lines down.
            adapted_board_state = game.board.state.copy().reshape((1, NB_ROWS * NB_COLUMNS))
            boards_from_game = np.insert(boards_from_game, 0, adapted_board_state, axis=0)
        while not game.board.finished:
            factor = 1 if game.turn == COMPUTER else -1  # learn all boards from the computer's perspective
            game.let_computer_play()
            adapted_board_state = factor * game.board.state.copy().reshape((1, NB_ROWS * NB_COLUMNS))
            boards_from_game = np.insert(boards_from_game, 0, adapted_board_state, axis=0)
        score = MAX_SCORE
        for board in boards_from_game:
            board_with_score = np.append(board, score)
            boards_with_score = np.insert(boards_with_score, 0, board_with_score, axis=0)
            if score > 0:
                score = -score  # the state that allowed the opponent to win should be scored as badly as the win itself
            else:
                score = -score * SCORE_DECREASE_RATE
        if (game_no > 0) & (game_no % nb_games_per_learning_iteration == 0):
            learning_strategy.learn_from(boards_with_score)
            boards_with_score = np.empty((0, NB_ROWS * NB_COLUMNS + 1))
    if len(boards_with_score) != 0:
        learning_strategy.learn_from(boards_with_score)
