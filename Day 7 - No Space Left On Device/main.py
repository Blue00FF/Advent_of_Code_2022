import re


def get_file_indices(split_input):
    file_indices = {}
    for index, line in enumerate(split_input):
        if re.search("\d+", line):
            file_indices.update({line: index})
    return file_indices


def print_dict_by_line(dictionary):
    for key, value in dictionary.items():
        print(f"{key} : {value}")


def print_list_by_line(listable):
    for value in listable:
        print(value)


def get_file_paths(split_input, file_indices):
    file_paths = {}
    for file_name, file_index in file_indices.items():
        pointer = file_index
        file_path = ""
        file_path += file_name.split()[1]
        current_dir = ""
        cd_mode, dir_mode = True, False
        while pointer >= 0:
            pointer -= 1
            location = split_input[pointer]
            if cd_mode and re.search("cd ", location):
                current_dir = location.split()[2]
                file_path = current_dir + "/" + file_path
                cd_mode, dir_mode = False, True
            if dir_mode and re.search("dir " + current_dir, location):
                cd_mode, dir_mode = True, False
        file_paths.update({file_name: file_path})
    return file_paths


def get_dir_indices(split_input):
    dir_indices = {}
    dir_indices.update({0: "//"})
    for index, line in enumerate(split_input):
        if re.search("dir ", line):
            dir_indices.update({index: line.split()[1]})
    return dir_indices


def get_dir_paths(split_input, dir_indices):
    dir_paths = []
    for dir_index, dir_name in dir_indices.items():
        pointer = dir_index
        dir_path = ""
        dir_path += dir_name
        current_dir = ""
        cd_mode, dir_mode = True, False
        while pointer >= 0:
            pointer -= 1
            location = split_input[pointer]
            if cd_mode and re.search("cd ", location):
                current_dir = location.split()[2]
                dir_path = current_dir + "/" + dir_path
                cd_mode, dir_mode = False, True
            if dir_mode and re.search("dir " + current_dir, location):
                cd_mode, dir_mode = True, False
        dir_paths.append(dir_path)
    return dir_paths


def get_dir_sizes(file_paths, dir_paths):
    dir_sizes = {}
    for dir_path in dir_paths:
        dir_size = 0
        for file_name, file_path in file_paths.items():
            if dir_path in file_path:
                dir_size += int(file_name.split()[0])
        dir_sizes.update({dir_path: dir_size})
    return dir_sizes


def find_small_dirs(dir_sizes):
    MAX_SIZE = 100000
    small_dirs = dict(filter(lambda item: int(item[1]) <= MAX_SIZE, dir_sizes.items()))
    return small_dirs


def get_total_size(dirs):
    total = 0
    for _, size in dirs.items():
        total += size
    return total


def get_dir_size_to_delete(dir_sizes):
    TOTAL_DISK_SPACE = 70000000
    UPDATE_FILE_SIZE = 30000000
    total_occupied_space = dir_sizes["//"]
    space_needed = UPDATE_FILE_SIZE - (TOTAL_DISK_SPACE - total_occupied_space)
    record_size_difference = float("inf")
    for _, dir_size in dir_sizes.items():
        if (
            dir_size >= space_needed
            and dir_size - space_needed <= record_size_difference
        ):
            record_size_difference = dir_size - space_needed
    return record_size_difference + space_needed


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    split_content = content.split("\n")
    file_indices = get_file_indices(split_content)
    file_paths = get_file_paths(split_content, file_indices)
    dir_indices = get_dir_indices(split_content)
    dir_paths = get_dir_paths(split_content, dir_indices)
    dir_sizes = get_dir_sizes(file_paths, dir_paths)
    small_dirs = find_small_dirs(dir_sizes)
    total_small_dirs_size = get_total_size(small_dirs)
    print(total_small_dirs_size)
    dir_size_to_delete = get_dir_size_to_delete(dir_sizes)
    print(dir_size_to_delete)
