from main import *

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

Square.convert_to_grid(test_input)
Square.determine_all_possible_moves()
print(Square.find_path_to_finish())
