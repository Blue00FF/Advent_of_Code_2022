from main import *

test_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_part_1():
    Piece.process_input(test_input)
    Block.generate_grid()
    Piece.start_part_1()
    assert Piece.tower_top == 3068
