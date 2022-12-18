from main import *

test_input_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def test_calculate_total_visited_length_2_input_1():
    rope = Rope(2)
    rope.set_commands(test_input_1)
    rope.start_movement()
    assert rope.calculate_total_visited() == 13


def test_calculate_total_visited_length_10_input_1():
    rope = Rope(10)
    rope.set_commands(test_input_1)
    rope.start_movement()
    assert rope.calculate_total_visited() == 1


def test_calculate_total_visited_length_10_input_2():
    rope = Rope(10)
    rope.set_commands(test_input_2)
    rope.start_movement()
    assert rope.calculate_total_visited() == 36


if __name__ == "__main__":
    rope = Rope(10)
    rope.set_commands(test_input_2)
    rope.start_movement()
