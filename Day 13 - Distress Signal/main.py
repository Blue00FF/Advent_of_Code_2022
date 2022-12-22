def parse_list_from_string(content):
    split_input = content.split("\n\n")
    for i in range(len(split_input)):
        split_input[i] = [
            eval(split_input[i].split("\n")[0]),
            eval(split_input[i].split("\n")[1]),
        ]
    return split_input


def compare_integers(left_int, right_int):
    if left_int < right_int:
        return True
    if left_int == right_int:
        return None
    else:
        return False


def evaluate_pair_of_elements(left_list, right_list, index):
    left_element = left_list[index]
    right_element = right_list[index]
    if type(left_element) == list and type(right_element) == int:
        return evaluate_pair_of_lists(left_element, [right_element])
    if type(left_element) == int and type(right_element) == int:
        return compare_integers(left_element, right_element)
    if type(left_element) == int and type(right_element) == list:
        return evaluate_pair_of_lists([left_element], right_element)
    if type(left_element) == list and type(right_element) == list:
        return evaluate_pair_of_lists(left_element, right_element)


def evaluate_pair_of_lists(left_list, right_list):
    limit_length = max(len(left_list), len(right_list))
    for i in range(limit_length):
        if i >= len(left_list):
            return True
        if i >= len(right_list):
            return False
        if evaluate_pair_of_elements(left_list, right_list, i) == None:
            continue
        if evaluate_pair_of_elements(left_list, right_list, i):
            return True
        else:
            return False


def find_correctly_sorted_indices(parsed_input):
    correctly_sorted_indices = []
    for i in range(len(parsed_input)):
        current_pair = parsed_input[i]
        if evaluate_pair_of_lists(current_pair[0], current_pair[1]):
            correctly_sorted_indices.append(i + 1)
    return correctly_sorted_indices


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    parsed_input = parse_list_from_string(content)
    correctly_sorted_indices = find_correctly_sorted_indices(parsed_input)
    print(sum(correctly_sorted_indices))
