from main import *

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

rope = Rope()
rope.set_commands(test_input)
rope.start_movement()


def test_calculate_total_visited():
    assert rope.calculate_total_visited() == 13
