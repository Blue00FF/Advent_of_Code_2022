from main import *

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
file_indices = get_file_indices(split_test_input)
file_paths = get_file_paths(split_test_input, file_indices)
dir_indices = get_dir_indices(split_test_input)
dir_paths = get_dir_paths(split_test_input, dir_indices)
dir_sizes = get_dir_sizes(file_paths, dir_paths)
small_dirs = find_small_dirs(dir_sizes)
total_small_dirs_size = get_total_size(small_dirs)
dir_size_to_delete = get_dir_size_to_delete(dir_sizes)


def test_get_file_indices():
    assert file_indices == {
        "14848514 b.txt": 3,
        "8504156 c.dat": 4,
        "29116 f": 9,
        "2557 g": 10,
        "62596 h.lst": 11,
        "584 i": 14,
        "4060174 j": 19,
        "8033020 d.log": 20,
        "5626152 d.ext": 21,
        "7214296 k": 22,
    }


def test_get_file_paths():
    assert file_paths == {
        "14848514 b.txt": "//b.txt",
        "8504156 c.dat": "//c.dat",
        "29116 f": "//a/f",
        "2557 g": "//a/g",
        "62596 h.lst": "//a/h.lst",
        "584 i": "//a/e/i",
        "4060174 j": "//d/j",
        "8033020 d.log": "//d/d.log",
        "5626152 d.ext": "//d/d.ext",
        "7214296 k": "//d/k",
    }


def test_get_dir_indices():
    assert dir_indices == {0: "//", 2: "a", 5: "d", 8: "e"}


def test_get_dir_paths():
    assert dir_paths == ["//", "//a", "//d", "//a/e"]


def test_get_dir_sizes():
    assert dir_sizes == {"//": 48381165, "//a": 94853, "//d": 24933642, "//a/e": 584}


def test_get_small_dirs():
    assert small_dirs == {"//a": 94853, "//a/e": 584}


def test_get_total_small_dirs_size():
    assert total_small_dirs_size == 95437


def test_get_dir_size_to_delete():
    assert dir_size_to_delete == 24933642
