class Rope:
    def __init__(self) -> None:
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.movement_counter = 0
        self.movement_direction = None
        self.commands = []
        self.history = []

    def set_commands(self, content):
        self.commands = content.split("\n")

    def leave_trail(self, grid):
        grid[self.tail_x][self.tail_y].is_visited = True

    def move_head(self):
        match self.movement_direction:
            case "U":
                self.head_x -= 1
            case "D":
                self.head_x += 1
            case "L":
                self.head_y -= 1
            case "R":
                self.head_y += 1
        self.movement_counter -= 1

    def move_tail(self):
        delta_x = self.head_x - self.tail_x
        delta_y = self.head_y - self.tail_y
        if delta_x == 0 and abs(delta_y) > 1:
            self.tail_y += delta_y // abs(delta_y)
        elif delta_y == 0 and abs(delta_x) > 1:
            self.tail_x += delta_x // abs(delta_x)
        elif (abs(delta_x) > 1 and abs(delta_y) == 1) or (
            abs(delta_y) > 1 and abs(delta_x) == 1
        ):
            self.tail_x += delta_x // abs(delta_x)
            self.tail_y += delta_y // abs(delta_y)

    def no_movement_left(self):
        return self.movement_counter == 0

    def get_next_command(self):
        self.movement_counter = int(self.commands[0].split()[1])
        self.movement_direction = self.commands[0].split()[0]
        self.commands.pop(0)

    def start_movement(self):
        while True:
            self.history.append((self.tail_x, self.tail_y))
            if self.no_movement_left():
                if len(self.commands) == 0:
                    break
                self.get_next_command()
            self.move_head()
            self.move_tail()

    def calculate_total_visited(self):
        return len(set(self.history))


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    rope = Rope()
    rope.set_commands(content)
    rope.start_movement()
    print(rope.calculate_total_visited())
