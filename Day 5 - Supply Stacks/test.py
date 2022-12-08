from main import move_crate, read_instructions

testing_input ="""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

split_input = testing_input.split("\n")[6:]


def test_read_instructions():
    assert read_instructions(split_input[0]) == (1, 2, 1)

def test_move_crate():
    stack_1 = ["Z", "N"]
    stack_2 = ["M", "C", "D"]
    stack_3 = ["P"]
    stacks = [stack_1, stack_2, stack_3]
    assert move_crate(stacks, 1, 2, 1) == [["Z", "N", "D"], ["M", "C"], ["P"]]
    assert move_crate(stacks, 3, 1, 3) == [[], ["M", "C"], ["P", "D", "N", "Z"]]