import functools


def parse_list_from_string(content):
    split_input = content.split("\n\n")
    for i in range(len(split_input)):
        split_input[i] = [
            eval(split_input[i].split("\n")[0]),
            eval(split_input[i].split("\n")[1]),
        ]
    return split_input


def parse_unnested_list_from_string(content):
    split_input = content.split("\n\n")
    result = []
    for i in range(len(split_input)):
        result.append(eval(split_input[i].split("\n")[0]))
        result.append(eval(split_input[i].split("\n")[1]))
    return result


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


def compare_elements(left_list, right_list):
    if evaluate_pair_of_lists(left_list, right_list):
        return -1
    else:
        return 1


def determine_index_product(content):
    unnested_input = parse_unnested_list_from_string(content)
    unnested_input.append([[2]])
    unnested_input.append([[6]])
    unnested_input.sort(key=functools.cmp_to_key(compare_elements))
    index_product = 1
    for index in range(len(unnested_input)):
        if unnested_input[index] in [[[2]], [[6]]]:
            index_product *= index + 1
    return index_product


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    parsed_input = parse_list_from_string(content)
    correctly_sorted_indices = find_correctly_sorted_indices(parsed_input)
    print(sum(correctly_sorted_indices))
    print(determine_index_product(content))
