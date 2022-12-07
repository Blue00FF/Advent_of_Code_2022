def find_common_item(rucksack):
    middle_point = len(rucksack)//2
    compartment_1, compartment_2 = rucksack[:middle_point], rucksack[middle_point:]
    found = False
    common_item = ""
    for letter_1 in compartment_1:
        for letter_2 in compartment_2:
            if letter_1 == letter_2:
                found = True
                common_item = letter_1
                break
        if found:
            break
    if common_item == "":
        raise Exception("No common item found!")
    return common_item

def find_letter_value(letter):
    if letter.islower():
        result = ord(letter) - 96
    elif letter.isupper():
        result = ord(letter) - 38
    else:
        raise Exception("Something went wrong!")
    return result

def find_badge_type(rucksack_1, rucksack_2, rucksack_3):
    found = False
    common_item = ""
    for letter_1 in rucksack_1:
        for letter_2 in rucksack_2:
            for letter_3 in rucksack_3:
                if letter_1 == letter_2 and letter_2 == letter_3:
                    found = True
                    common_item = letter_1
                    break
            if found:
                break
        if found:
            break
    if common_item == "":
        raise Exception("No common item found!")
    return common_item

def group_dispenser(index, split_content):
    return split_content[3*index], split_content[3*index + 1], split_content[3*index + 2]


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    split_content = content.split("\n")
    total_value = 0
    for rucksack in split_content:
        common_item = find_common_item(rucksack)
        item_value = find_letter_value(common_item)
        total_value += item_value
    print(total_value)
    n_of_elves = len(split_content)
    total_value = 0
    for i in range(n_of_elves//3):
        badge_type = find_badge_type(*group_dispenser(index = i, split_content=split_content))
        badge_value = find_letter_value(badge_type)
        total_value += badge_value
    print(total_value)