import random

from game.Board import Board
from game.Constants import HUMAN, COMPUTER
from game.Screen import Screen


# This class represents a connect4 game.  It can optionally show the moves of the game on the screen.
# You need to pass in a strategy (from the learning folder) to create a game.  That strategy determines
# the computer's moves.  If you don't want to play against the computer, but let the computer play
# against itself, you can pass a second strategy.  You can pass None for the second strategy if you want
# to play yourself.
class Game:

    def __init__(self, show_moves, computer_strategy, other_strategy):
        self.show_moves = show_moves
        self.nb_moves = 0
        if show_moves:
            self.screen = Screen()
        self.turn = None
        self.board = None
        self.strategy = computer_strategy
        self.other_strategy = other_strategy

    # Start a new game.  It is randomly decided who should start.
    def start(self):
        self.turn = HUMAN if random.choice([True, False]) else COMPUTER
        self.nb_moves = 0
        self.board = Board()
        if self.show_moves:
            self.screen.draw_empty()
        if self.turn == COMPUTER:
            self.let_computer_play()

    def __switch_turn(self):
        self.turn = -self.turn

    # Play on the specified location of the screen - used for when you are playing the computer,
    # and click on a column
    def play(self, coordinate):
        if self.board.finished:
            self.start()
        else:
            column_clicked = Screen.get_column(coordinate)
            if self.board.can_play(column_clicked):
                done, _ = self.__column_played(column_clicked)
                if not done:
                    self.let_computer_play()

    # Returns if the game is done, and if it's a win or a tie
    def __column_played(self, col):
        self.nb_moves = self.nb_moves + 1
        row_played, win = self.board.play(self.turn, col)
        if self.show_moves:
            self.screen.play(self.turn, row_played, col)
        if win:
            if self.show_moves:
                self.screen.display_win(self.turn)
            return True, True
        elif self.board.finished:
            if self.show_moves:
                self.screen.display_tie()
            return True, False
        else:
            self.__switch_turn()
            return False, False

    # This method gets called automatically when the computer needs to play.
    # You can also call it manually if you want to let the second playing strategy play for the human's turn.
    # Returns if the game is done, and if it's a win or a tie
    def let_computer_play(self):
        strategy_to_play = self.strategy if self.turn == COMPUTER else self.other_strategy
        column_played = strategy_to_play.next_move(self.turn, self.board)
        return self.__column_played(column_played)

