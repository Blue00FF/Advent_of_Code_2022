from main import *

test_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_part_1():
    Piece.process_input(test_input)
    Block.generate_grid()
    Piece.start_falling_rocks_part_1()
    assert Piece.tower_top == 3068


def test_part_2():
    Piece.process_input(test_input)
    Block.generate_grid()
    Block.GRID_HEIGHT = 1000000
    assert Piece.start_test_falling_rocks() == 1514285714288
