from main import *

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_find_path_from_start_to_finish():
    Square.convert_to_grid(test_input)
    Square.determine_all_possible_moves()
    current_record = Square.find_path_to_finish()
    assert current_record == 31


def test_find_scenic_path():
    Square.convert_to_grid(test_input)
    Square.determine_all_possible_moves()
    current_record = Square.find_path_to_finish()
    previous_start = (0, 0)
    for possible_start in Square.scenic_starts:
        Square.reset_grid(previous_start, possible_start)
        new_path_length = Square.find_path_to_finish()
        if new_path_length < current_record:
            current_record = new_path_length
        previous_start = possible_start
    assert current_record == 29
