from main import *

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def test_sand_counter():
    Block.process_input(test_input)
    Block.start_sand()
    assert Block.sand_counter == 24
