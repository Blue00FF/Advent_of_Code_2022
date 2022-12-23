class Block:
    grid = []
    GRID_HEIGHT = 1000
    GRID_LENGTH = 1000
    active_block = (0, 500)
    sand_counter = 0
    is_finished = False
    floor_height = 0

    def start_sand_without_floor():
        Block.sand_counter = 0
        while not Block.is_finished:
            Block.grid[Block.active_block[0]][Block.active_block[1]].endless_fall()

    def start_sand_with_floor():
        Block.sand_counter = 0
        for y in range(Block.GRID_LENGTH):
            Block.grid[Block.floor_height + 2][y].turn_into_rock()
        Block.is_finished = False
        while not Block.is_finished:
            Block.grid[Block.active_block[0]][Block.active_block[1]].finite_fall()

    def process_input(content):
        Block.generate_grid()
        processed_input = content.split("\n")
        for i in range(len(processed_input)):
            processed_input[i] = processed_input[i].split(" -> ")
        for line in processed_input:
            for index in range(1, len(line)):
                previous_coordinates = list(map(int, line[index - 1].split(",")))
                current_coordinates = list(map(int, line[index].split(",")))
                if (
                    current_coordinates[0] < previous_coordinates[0]
                    or current_coordinates[1] < previous_coordinates[1]
                ):
                    current_coordinates, previous_coordinates = (
                        previous_coordinates,
                        current_coordinates,
                    )
                if current_coordinates[1] > Block.floor_height:
                    Block.floor_height = current_coordinates[1]
                for x in range(previous_coordinates[1], current_coordinates[1] + 1):
                    Block.grid[x][previous_coordinates[0]].turn_into_rock()
                for y in range(previous_coordinates[0], current_coordinates[0] + 1):
                    Block.grid[previous_coordinates[1]][y].turn_into_rock()

    def generate_grid():
        Block.grid = []
        for x in range(Block.GRID_HEIGHT):
            Block.grid.append([])
            for y in range(Block.GRID_LENGTH):
                Block.grid[x].append(Block(x, y, "air"))

    def visualise_grid():
        for x in range(12):
            for y in range(488, 513):
                if Block.grid[x][y].is_air():
                    print(".", sep="", end="")
                elif Block.grid[x][y].block_type == "sand":
                    print("+", sep="", end="")
                else:
                    print("#", sep="", end="")
            print()

    def __init__(self, x_pos, y_pos, block_type):
        self.block_type = block_type
        self.x_pos = x_pos
        self.y_pos = y_pos

    def endless_fall(self):
        down = Block.grid[self.x_pos + 1][self.y_pos]
        down_left = Block.grid[self.x_pos + 1][self.y_pos - 1]
        down_right = Block.grid[self.x_pos + 1][self.y_pos + 1]
        if self.x_pos >= Block.GRID_HEIGHT - 2:
            Block.active_block = (0, 500)
            Block.is_finished = True
        elif down.is_air():
            down.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down.x_pos, down.y_pos)
        elif down_left.is_air():
            down_left.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down_left.x_pos, down_left.y_pos)
        elif down_right.is_air():
            down_right.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down_right.x_pos, down_right.y_pos)
        else:
            Block.sand_counter += 1
            Block.active_block = (0, 500)
            Block.grid[0][500].turn_into_sand()

    def finite_fall(self):
        down = Block.grid[self.x_pos + 1][self.y_pos]
        down_left = Block.grid[self.x_pos + 1][self.y_pos - 1]
        down_right = Block.grid[self.x_pos + 1][self.y_pos + 1]
        if down.is_air():
            down.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down.x_pos, down.y_pos)
        elif down_left.is_air():
            down_left.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down_left.x_pos, down_left.y_pos)
        elif down_right.is_air():
            down_right.turn_into_sand()
            self.turn_into_air()
            Block.active_block = (down_right.x_pos, down_right.y_pos)
        else:
            Block.sand_counter += 1
            if Block.active_block == (0, 500):
                Block.is_finished = True
            Block.active_block = (0, 500)
            Block.grid[0][500].turn_into_sand()

    def turn_into_rock(self):
        self.block_type = "rock"
        self.is_falling = False

    def turn_into_air(self):
        self.block_type = "air"
        self.is_falling = False

    def turn_into_sand(self):
        self.block_type = "sand"
        self.is_falling = True

    def is_air(self):
        return self.block_type == "air"


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Block.process_input(content)
    Block.start_sand_without_floor()
    print(Block.sand_counter)
    Block.process_input(content)
    Block.start_sand_with_floor()
    print(Block.sand_counter)
