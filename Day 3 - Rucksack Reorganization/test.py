from main import find_common_item, find_letter_value, find_badge_type

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_input_split = test_input.split("\n")

expected_test_result = [
    "p",
    "L",
    "P",
    "v",
    "t",
    "s"
]

expected_letter_value = [
    16,
    38,
    42,
    22,
    20,
    19
]

def test_find_common_item():
    for index, rucksack in enumerate(test_input_split):
        assert find_common_item(rucksack) == expected_test_result[index]

def test_find_letter_value():
    for index, letter in enumerate(expected_test_result):
        assert find_letter_value(letter) == expected_letter_value[index]

def test_find_badge_type():
    assert (find_badge_type(test_input_split[0], test_input_split[1], test_input_split[2])) == "r"
    assert (find_badge_type(test_input_split[3], test_input_split[4], test_input_split[5])) == "Z"
    