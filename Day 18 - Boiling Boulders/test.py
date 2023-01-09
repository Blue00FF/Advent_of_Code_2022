from main import *

test_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def test_calculate_total_surface_area():
    Cube.GRID_SIZE = 10
    Cube.generate_grid()
    Cube.process_input(test_input)
    Cube.calculate_surface_areas()
    assert Cube.calculate_total_surface_area() == 64
