from main import *

test_input = """30373
25512
65332
33549
35390"""

Tree.FOREST_GRID_HEIGHT = 5
Tree.FOREST_GRID_WIDTH = 5
forest = Tree.generate_forest(test_input)
Tree.calculate_total_visibility_count(forest)
Tree.calculate_top_scenic_score(forest)


def test_calculate_total_visibility_count():
    assert Tree.total_visibility_count == 21


def test_calculate_top_scenic_score():
    assert Tree.top_scenic_score == 8
