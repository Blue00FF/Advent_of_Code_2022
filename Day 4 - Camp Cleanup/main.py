def get_ranges(input):
    input_1, input_2 = input.split(",")[0], input.split(",")[1]
    range_1 = [x for x in range(int(input_1.split("-")[0]), int(input_1.split("-")[1]) + 1)]
    range_2 = [x for x in range(int(input_2.split("-")[0]), int(input_2.split("-")[1]) + 1)]
    return range_1, range_2

def get_intersection(range_1, range_2):
    set_1 = set(range_1)
    set_2 = set(range_2)
    return list(set_1 & set_2)

def is_contained(range_1, range_2):
    intersection = get_intersection(range_1, range_2)
    intersection.sort()
    if range_1 == intersection or range_2 == intersection:
        return 1
    else:
        return 0

def is_contained_counter(split_content):
    contained_counter = 0
    for element in split_content:
        ranges = get_ranges(element)
        contained_counter += is_contained(*ranges)
    return contained_counter

def is_intersection_counter(split_content):
    intersection_counter = 0
    for element in split_content:
        ranges = get_ranges(element)
        if len(get_intersection(*ranges))>0:
            intersection_counter += 1
    return intersection_counter

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    split_content = content.split("\n")
    print(is_contained_counter(split_content))
    print(is_intersection_counter(split_content))