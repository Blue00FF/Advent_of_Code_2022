import re

def remove_all_occurrences(element, list):
    while element in list:
        list.remove(element)

def get_file_size(split_input):
    file_size_dict = {}
    file_list = [x for x in split_input if not re.search("\$ ", x)]
    file_list = [x for x in file_list if not re.search("dir ", x)]
    for file in file_list:
        file_size_dict.update({file.split()[1] : int(file.split()[0])})
    return file_size_dict 
    
def get_file_location(split_input, file_size_dict):
    file_location_dict = {}
    for file_name in file_size_dict.keys():
        file_index = None
        for index, line in enumerate(split_input):
            if re.search(" " + file_name, line):
                file_index = index
                break
        index = file_index
        while index >= 0:
            index -= 1
            if re.search("cd ", split_input[index]):
                file_location_dict.update({file_name : split_input[index].split()[2]})
                break
    return file_location_dict

def get_folder_location(split_input):
    folder_location_dict = {}
    folder_position_dict = {}
    for index, line in enumerate(split_input):
        if re.search("dir ", line):
            folder_position_dict.update({line.split()[1] : index})
    for folder_name, folder_index in folder_position_dict.items():
        index = folder_index
        while index >= 0:
            index -= 1
            if re.search("cd ", split_input[index]):
                folder_location_dict.update({folder_name : split_input[index].split()[2]})
                break
    return folder_location_dict

def get_folder_size(file_size_dict, file_location_dict, folder_location_dict):
    folder_size_dict = {}
    folder_list = list(folder_location_dict.keys())
    folder_list.reverse()
    for folder_name in folder_list:
        folder_size = 0
        for file_name, parent_folder in file_location_dict.items():
            if parent_folder == folder_name:
                folder_size += file_size_dict[file_name]
        for child_folder, parent_folder in folder_location_dict.items():
            if parent_folder == folder_name:
                folder_size += folder_size_dict[child_folder]
        folder_size_dict.update({folder_name: folder_size})
    return folder_size_dict        

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    split_content = content.split("\n")
    file_size_dict = get_file_size(split_content)
    file_location_dict = get_file_location(split_content, file_size_dict)
    folder_location_dict = get_folder_location(split_content)
    folder_size_dict = get_folder_size(file_size_dict, file_location_dict, folder_location_dict)
    print(folder_size_dict)