from main import *

test_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

Piece.process_input(test_input)
Block.generate_grid()
Piece.start_part_1()
Block.visualise_grid()
print(Piece.tower_top)
