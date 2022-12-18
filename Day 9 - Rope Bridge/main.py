class Rope:
    def __init__(self, rope_length) -> None:
        self.ROPE_LENGTH = rope_length
        self.nodes_x = [0] * rope_length
        self.nodes_y = [0] * rope_length
        self.movement_counter = 0
        self.movement_direction = None
        self.commands = []
        self.history = []

    def set_commands(self, content):
        self.commands = content.split("\n")

    def move_head(self):
        match self.movement_direction:
            case "U":
                self.nodes_x[0] -= 1
            case "D":
                self.nodes_x[0] += 1
            case "L":
                self.nodes_y[0] -= 1
            case "R":
                self.nodes_y[0] += 1
        self.movement_counter -= 1

    def move_tail(self):
        for index in range(1, self.ROPE_LENGTH):
            delta_x = self.nodes_x[index - 1] - self.nodes_x[index]
            delta_y = self.nodes_y[index - 1] - self.nodes_y[index]
            if delta_x == 0 and abs(delta_y) > 1:
                self.nodes_y[index] += delta_y // abs(delta_y)
            elif delta_y == 0 and abs(delta_x) > 1:
                self.nodes_x[index] += delta_x // abs(delta_x)
            elif (abs(delta_x) > 1 and abs(delta_y) == 1) or (
                abs(delta_y) > 1 and abs(delta_x) == 1
            ):
                self.nodes_x[index] += delta_x // abs(delta_x)
                self.nodes_y[index] += delta_y // abs(delta_y)

    def no_movement_left(self):
        return self.movement_counter == 0

    def get_next_command(self):
        self.movement_counter = int(self.commands[0].split()[1])
        self.movement_direction = self.commands[0].split()[0]
        self.commands.pop(0)

    def start_movement(self):
        self.history = []
        while True:
            self.history.append((self.nodes_x[-1], self.nodes_y[-1]))
            if self.no_movement_left():
                if len(self.commands) == 0:
                    break
                self.get_next_command()
            self.move_head()
            self.move_tail()
            # self.visualise_rope()

    def calculate_total_visited(self):
        return len(set(self.history))

    def visualise_rope(self):
        print()
        for i in zip(self.nodes_x, self.nodes_y):
            print(i)


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    rope_1 = Rope(2)
    rope_1.set_commands(content)
    rope_1.start_movement()
    print(rope_1.calculate_total_visited())
    rope_2 = Rope(10)
    rope_2.set_commands(content)
    rope_2.start_movement()
    print(rope_2.calculate_total_visited())
