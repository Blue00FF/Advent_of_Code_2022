from main import *

test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

parsed_input = parse_list_from_string(test_input)


def test_find_correctly_sorted_indices():
    assert find_correctly_sorted_indices(parsed_input) == [1, 2, 4, 6]


def test_sum_of_correctly_sorted_indices():
    assert sum(find_correctly_sorted_indices(parsed_input)) == 13
