import numpy as np
from game.Constants import NB_COLUMNS, NB_ROWS, EMPTY


# This class represents the state of the connect4 board - independent of the display logic.
class Board:

    def __init__(self):
        self.state = np.zeros((NB_ROWS, NB_COLUMNS))
        self.finished = False

    def can_play(self, col):
        return (not self.finished) & (col >= 0) & (self.state[NB_ROWS-1][col] == EMPTY)

    # precondition: can_play(col) == True
    def play(self, player, col):
        row = 0
        while self.state[row][col] != EMPTY:
            row = row+1
        self.state[row][col] = player
        win = self.detect_win(row, col)
        return row, win

    # precondition: the given col has just been played
    def undo(self, col):
        row = NB_ROWS - 1
        while self.state[row][col] == EMPTY:
            row = row-1
        self.state[row][col] = EMPTY
        self.finished = False

    def detect_win(self, row, col):
        player = self.state[row][col]

        # E.g. if you have 2 pieces from the same player to the left, and 1 to the right,
        # you have 2 + 1 + 1 (the piece that was played) = 4 in a row
        # => the sum of the pieces in opposite directions should be >= 3

        # Horizontal
        if self.__count_player_in_direction(player, row, col, 0, -1) \
                + self.__count_player_in_direction(player, row, col, 0, 1) >= 3:
            return self.finish_game(True)
        # Vertical
        if self.__count_player_in_direction(player, row, col, -1, 0) \
                + self.__count_player_in_direction(player, row, col, 1, 0) >= 3:
            return self.finish_game(True)
        # Diagonal 1
        if self.__count_player_in_direction(player, row, col, -1, -1) \
                + self.__count_player_in_direction(player, row, col, 1, 1) >= 3:
            return self.finish_game(True)
        # Diagonal 2
        if self.__count_player_in_direction(player, row, col, -1, 1) \
                + self.__count_player_in_direction(player, row, col, 1, -1) >= 3:
            return self.finish_game(True)

        legal_moves = self.get_legal_moves()
        if len(legal_moves) == 0:
            return self.finish_game(False)

        return False

    def __count_player_in_direction(self, player, row, col, direction_row, direction_col):
        next_col = col + direction_col
        next_row = row + direction_row
        if (next_col < 0) | (next_row < 0) | (next_col >= NB_COLUMNS) | (next_row >= NB_ROWS):
            return 0
        if self.state[next_row][next_col] != player:
            return 0
        return 1 + self.__count_player_in_direction(player, next_row, next_col, direction_row, direction_col)

    def finish_game(self, win):
        self.finished = True
        return win

    def get_legal_moves(self):
        legal_moves = []
        for col in range(NB_COLUMNS):
            if self.can_play(col):
                legal_moves.append(col)
        return legal_moves
