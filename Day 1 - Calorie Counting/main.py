if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    splitted_string = content.split("\n\n")
    elf_calories_list = []

    for elf_string in splitted_string:
        elf_bag = []
        elf_string = elf_string.replace("\n", " ")
        elf_split_string = elf_string.split()
        for candy in elf_split_string:
            elf_bag.append(int(candy))
        elf_calories_list.append(sum(elf_bag))
    elf_calories_list.sort(reverse=True)
    print(elf_calories_list[0])
    print(sum(elf_calories_list[:3]))
