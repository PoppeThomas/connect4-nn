import numpy as np
from Constants import NB_COLUMNS, NB_ROWS, EMPTY


class Board:

    def __init__(self):
        self.state = np.zeros((NB_COLUMNS, NB_ROWS))
        self.finished = False

    def can_play(self, col):
        return (not self.finished) & (col >= 0) & (self.state[col][NB_ROWS-1] == EMPTY)

    # precondition: can_play(col) == True
    def play(self, player, col):
        row = 0
        while self.state[col][row] != EMPTY:
            row = row+1
        self.state[col][row] = player
        win = self.detect_win(col, row)
        return row, win

    def detect_win(self, col, row):
        player = self.state[col][row]

        # E.g. if you have 2 pieces from the same player to the left, and 1 to the right,
        # you have 2 + 1 + 1 (the piece that was played) = 4 in a row
        # => the sum of the pieces in opposite directions should be >= 3

        # Horizontal
        if self.count_player_in_direction(player, col, row, -1, 0) \
                + self.count_player_in_direction(player, col, row, 1, 0) >= 3:
            return self.finish_game(True)
        # Vertical
        if self.count_player_in_direction(player, col, row, 0, -1) \
                + self.count_player_in_direction(player, col, row, 0, 1) >= 3:
            return self.finish_game(True)
        # Diagonal 1
        if self.count_player_in_direction(player, col, row, -1, -1) \
                + self.count_player_in_direction(player, col, row, 1, 1) >= 3:
            return self.finish_game(True)
        # Diagonal 2
        if self.count_player_in_direction(player, col, row, 1, -1) \
                + self.count_player_in_direction(player, col, row, -1, 1) >= 3:
            return self.finish_game(True)

        legal_moves = self.get_legal_moves()
        if len(legal_moves) == 0:
            return self.finish_game(False)

        return False

    def count_player_in_direction(self, player, col, row, direction_col, direction_row):
        next_col = col + direction_col
        next_row = row + direction_row
        if (next_col < 0) | (next_row < 0) | (next_col >= NB_COLUMNS) | (next_row >= NB_ROWS):
            return 0
        if self.state[next_col][next_row] != player:
            return 0
        return 1 + self.count_player_in_direction(player, next_col, next_row, direction_col, direction_row)

    def finish_game(self, win):
        self.finished = True
        return win

    def get_legal_moves(self):
        legal_moves = []
        for col in range(NB_COLUMNS):
            if self.can_play(col):
                legal_moves.append(col)
        return legal_moves
