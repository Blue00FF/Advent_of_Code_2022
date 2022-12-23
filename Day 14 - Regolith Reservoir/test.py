from main import *

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

Block.GRID_HEIGHT = 20
Block.GRID_LENGTH = 600


def test_sand_counter_without_floor():
    Block.process_input(test_input)
    Block.start_sand_without_floor()
    assert Block.sand_counter == 24


def test_sand_counter_with_floor():
    Block.process_input(test_input)
    Block.start_sand_with_floor()
    assert Block.sand_counter == 93
