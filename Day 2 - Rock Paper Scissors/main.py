def calculate_match_score_part_1(opponent_move, player_move):
    moves_values = {
            "A": 1,
            "B": 2,
            "C": 3,
            "X": 1,
            "Y": 2,
            "Z": 3 
    }
    match_value = moves_values[player_move] - moves_values[opponent_move]
    score = moves_values[player_move]
    if match_value == 0:
        score += 3 
    elif match_value in (1, -2):
        score += 6
    elif match_value in (-1, +2):
        score += 0
    else:
        raise Exception("Something went wrong!")
    return score

def calculate_match_score_part_2(opponent_move, match_outcome):
    moves_values = {
        "A": 1,
        "B": 2,
        "C": 3,
        }
    outcome_values = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    score = outcome_values[match_outcome]
    opponent_value = moves_values[opponent_move]
    if match_outcome == "Y":
        score += opponent_value
    elif match_outcome == "X":
        if opponent_value - 1 > 0: 
            score += opponent_value - 1
        else:
            score += 3
    elif match_outcome == "Z":
        if opponent_value + 1 < 4:
            score += opponent_value + 1
        else:
            score += 1
    else:
        raise Exception("Something went wrong!")
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    splitted_string = content.split("\n")
    total_score = 0
    for round in splitted_string:
        opponent_move = round[0]
        player_move = round[-1]
        total_score += calculate_match_score_part_1(opponent_move=opponent_move, player_move=player_move)
    print(total_score)
    total_score = 0
    for round in splitted_string:
        opponent_move = round[0]
        match_outcome = round[-1]
        total_score += calculate_match_score_part_2(opponent_move=opponent_move, match_outcome=match_outcome)
    print(total_score)