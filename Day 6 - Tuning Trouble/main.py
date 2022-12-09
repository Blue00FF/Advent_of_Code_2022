def find_packet_marker(input):
    output = -1
    for i in range(len(input) - 4):
        slice = input[i:i+4]
        if len(slice) == len(set(slice)):
            output = i + 4
            break
    if output == -1:
        raise Exception("The output value has not been changed!")
    return output

def find_message_marker(input):
    output = -1
    for i in range(len(input) - 14):
        slice = input[i:i+14]
        if len(slice) == len(set(slice)):
            output = i + 14
            break
    if output == -1:
        raise Exception("The output value has not been changed!")
    return output

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    print(find_packet_marker(content))
    print(find_message_marker(content))