starting_crates = """
                [M]     [W] [M]    
            [L] [Q] [S] [C] [R]    
            [Q] [F] [F] [T] [N] [S]
    [N]     [V] [V] [H] [L] [J] [D]
    [D] [D] [W] [P] [G] [R] [D] [F]
[T] [T] [M] [G] [G] [Q] [N] [W] [L]
[Z] [H] [F] [J] [D] [Z] [S] [H] [Q]
[B] [V] [B] [T] [W] [V] [Z] [Z] [M]
 1   2   3   4   5   6   7   8   9 
"""

def convert_input_to_stack(starting_input):
    stacks = []
    split_input = starting_input.split("\n")[1:]
    n_stacks = int(split_input[-2][-2])
    for _ in range(n_stacks):
        stacks.append([])
    for i in range(len(split_input) - 2):
        line = split_input[len(split_input) - 3 - i]
        line = line.replace("[", " ")
        line = line.replace("]", " ")
        for j in range(n_stacks):
            element = line[4*j + 1]
            if element != " ":
                stacks[j].append(element)
    return stacks

def move_crate_9000(stacks, n_crates, from_stack, to_stack):
    for _ in range(n_crates):
        top_crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(top_crate)

def move_crate_9001(stacks, n_crates, from_stack, to_stack):
    stacks[to_stack - 1] += stacks[from_stack - 1][-n_crates:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-n_crates]

def read_instructions(line):
    split_instructions = line.split()
    split_instructions.remove("move")
    split_instructions.remove("from")
    split_instructions.remove("to")
    return int(split_instructions[0]), int(split_instructions[1]), int(split_instructions[2])

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    split_content = content.split("\n")[10:]
    stacks = convert_input_to_stack(starting_crates)
    for line in split_content:
        instructions = read_instructions(line)
        move_crate_9000(stacks, *instructions)
    print(stacks)
    stacks = convert_input_to_stack(starting_crates)
    for line in split_content:
        instructions = read_instructions(line)
        move_crate_9001(stacks, *instructions)
    print(stacks)
    
