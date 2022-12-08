from main import get_ranges, get_intersection, is_contained, is_contained_counter, is_intersection_counter

testing_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

split_testing_input = testing_input.split("\n")

def test_get_ranges():
    assert get_ranges(split_testing_input[0]) == ([2, 3, 4],[6, 7, 8])
    assert get_ranges(split_testing_input[1]) == ([2, 3],[4, 5])
    assert get_ranges(split_testing_input[2]) == ([5, 6, 7],[7, 8, 9])
    assert get_ranges("71-77,70-78") == ([71, 72, 73, 74, 75, 76, 77],[70, 71, 72, 73, 74, 75, 76, 77, 78])

def test_get_intersection():
    assert get_intersection([5, 6, 7],[7, 8, 9]) == [7]
    assert get_intersection([71, 72, 73, 74, 75, 76, 77],[70, 71, 72, 73, 74, 75, 76, 77, 78]) == [71, 72, 73, 74, 75, 76, 77]

def test_get_empty_intersection():
    assert get_intersection([2, 3, 4],[6, 7, 8]) == []
    assert get_intersection([2, 3],[4, 5]) == []

def test_is_contained():
    assert is_contained(*([5, 6, 7],[7])) == 1
    assert is_contained(*([7], [5, 6, 7])) == 1
    assert is_contained(*([71, 72, 73, 74, 75, 76, 77],[70, 71, 72, 73, 74, 75, 76, 77, 78])) == 1

def test_is_not_contained():
    assert is_contained(*([5, 6, 7],[7, 8, 9])) == 0

def test_is_contained_counter():
    assert is_contained_counter(split_testing_input) == 2

def test_is_intersection_counter():
    assert is_intersection_counter(split_testing_input) == 4