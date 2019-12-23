from game.Board import Board
from game.Constants import HUMAN, COMPUTER


def test_detect_win_vertical():
    board = Board()
    row, win = board.play(HUMAN, 0)
    assert not win
    row, win = board.play(HUMAN, 0)
    assert not win
    row, win = board.play(HUMAN, 0)
    assert not win
    row, win = board.play(HUMAN, 0)
    assert win


def test_detect_win_horizontal():
    board = Board()
    row, win = board.play(COMPUTER, 0)
    assert not win
    row, win = board.play(COMPUTER, 1)
    assert not win
    row, win = board.play(COMPUTER, 3)
    assert not win
    row, win = board.play(COMPUTER, 2)
    assert win


def test_detect_win_horizontal_not_same_player():
    board = Board()
    row, win = board.play(COMPUTER, 0)
    assert not win
    row, win = board.play(HUMAN, 1)
    assert not win
    row, win = board.play(COMPUTER, 3)
    assert not win
    row, win = board.play(COMPUTER, 2)
    assert not win


def test_detect_win_diagonal_1():
    board = Board()
    row, win = board.play(COMPUTER, 0)
    assert not win
    row, win = board.play(HUMAN, 1)
    row, win = board.play(COMPUTER, 1)
    assert not win
    row, win = board.play(HUMAN, 2)
    row, win = board.play(HUMAN, 2)
    row, win = board.play(COMPUTER, 2)
    assert not win
    row, win = board.play(HUMAN, 3)
    row, win = board.play(COMPUTER, 3)
    row, win = board.play(HUMAN, 3)
    row, win = board.play(COMPUTER, 3)
    assert win


def test_detect_win_diagonal_2():
    board = Board()
    row, win = board.play(COMPUTER, 3)
    assert not win
    row, win = board.play(HUMAN, 2)
    row, win = board.play(COMPUTER, 2)
    assert not win
    row, win = board.play(HUMAN, 0)
    row, win = board.play(COMPUTER, 0)
    row, win = board.play(HUMAN, 0)
    row, win = board.play(COMPUTER, 0)
    assert not win
    row, win = board.play(HUMAN, 1)
    row, win = board.play(HUMAN, 1)
    row, win = board.play(COMPUTER, 1)
    assert win


