from main import find_packet_marker, find_message_marker

test_inputs = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

test_packet_markers = [
    7,
    5,
    6,
    10,
    11
]

test_message_markers = [
    19,
    23,
    23,
    29,
    26
]

def test_find_packet_marker():
    for i in range(len(test_inputs)):
        assert find_packet_marker(test_inputs[i]) == test_packet_markers[i]

def test_find_message_marker():
    for i in range(len(test_inputs)):
        assert find_message_marker(test_inputs[i]) == test_message_markers[i]