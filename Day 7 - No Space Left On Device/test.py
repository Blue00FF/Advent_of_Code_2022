from main import get_file_location, get_file_size, get_folder_location, get_folder_size

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

split_test_input = test_input.split("\n")
file_size_dict = get_file_size(split_test_input)
file_location_dict = get_file_location(split_test_input, file_size_dict)
folder_location_dict = get_folder_location(split_test_input)
folder_size_dict = get_folder_size(file_size_dict, file_location_dict, folder_location_dict)

def test_get_file_size():
    assert file_size_dict == {"i": 584, "f": 29116, "g": 2557, "h.lst": 62596, "b.txt": 14848514, "c.dat": 8504156, "j": 4060174, "d.log": 8033020, "d.ext": 5626152,"k": 7214296}

def test_get_file_location():
    assert file_location_dict == {"i": "e", "f": "a", "g": "a", "h.lst": "a", "b.txt": "/", "c.dat": "/", "j": "d", "d.log": "d", "d.ext": "d","k": "d"}

def test_get_folder_location():
    assert folder_location_dict == {"a": "/", "d": "/", "e": "a"}

def test_get_folder_size():
    assert folder_size_dict == {"e": 584, "a": 94853, "d": 24933642}
    
print(folder_size_dict)