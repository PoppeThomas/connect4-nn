import random
from Board import Board
from Constants import HUMAN, COMPUTER
from RandomStrategy import RandomStrategy
from Screen import Screen


class Game:

    def __init__(self):
        self.screen = Screen()
        self.turn = None
        self.board = None
        self.strategy = RandomStrategy()

    def start(self):
        self.turn = HUMAN if random.choice([True, False]) else COMPUTER
        self.board = Board()
        self.screen.draw_empty()
        if self.turn == COMPUTER:
            self.let_computer_play()

    def __switch_turn(self):
        self.turn = -self.turn

    def play(self, coordinate):
        if self.board.finished:
            self.start()
        else:
            column_clicked = Screen.get_column(coordinate)
            if self.board.can_play(column_clicked):
                done = self.column_played(column_clicked)
                if not done:
                    self.let_computer_play()

    def column_played(self, col):
        row_played, win = self.board.play(self.turn, col)
        self.screen.play(self.turn, col, row_played)
        if win:
            self.screen.display_win(self.turn)
            return True
        elif self.board.finished:
            self.screen.display_tie()
            return True
        else:
            self.__switch_turn()
            return False

    def let_computer_play(self):
        legal_moves = self.board.get_legal_moves()
        column_played = self.strategy.next_move(legal_moves)
        self.column_played(column_played)

