from main import calculate_match_score_part_1, calculate_match_score_part_2

def test_win_part_1():
    assert calculate_match_score_part_1("A", "Y") == 8

def test_loss_part_1():
    assert calculate_match_score_part_1("B", "X") == 1

def test_draw_part_1():
    assert calculate_match_score_part_1("C", "Z") == 6

def test_win_part_2():
    assert calculate_match_score_part_2("A", "Y") == 4

def test_loss_part_2():
    assert calculate_match_score_part_2("B", "X") == 1

def test_draw_part_2():
    assert calculate_match_score_part_2("C", "Z") == 7