class Square:
    grid = []
    history = []
    GRID_HEIGHT = None
    GRID_WIDTH = None

    def convert_to_grid(content):
        Square.grid = []
        grid_heights = []
        split_content = content.split("\n")
        for i in range(len(split_content)):
            grid_heights.append([*split_content[i]])
        Square.GRID_HEIGHT = len(grid_heights)
        Square.GRID_WIDTH = len(grid_heights[0])
        for x in range(Square.GRID_HEIGHT):
            Square.grid.append([])
            for y in range(Square.GRID_WIDTH):
                Square.grid[x].append(Square(x, y, grid_heights[x][y]))

    def determine_all_possible_moves():
        for row in Square.grid:
            for square in row:
                square.determine_possible_moves()

    def find_path_to_finish():
        solution_found = False
        i = 0
        while not solution_found and i < 10000:
            i += 1
            temp_history = Square.history.copy()
            Square.history = []
            for element in temp_history:
                x, y = element[-1]
                current_pos = Square.grid[x][y]
                if current_pos.is_finish:
                    Square.history.append(element)
                    solution_found = True
                    continue
                if current_pos.is_stuck():
                    continue
                if current_pos.up_accessible and not current_pos.up_attempted:
                    Square.history.append(element + [(x - 1, y)])
                    current_pos.up_attempted = True
                if current_pos.down_accessible and not current_pos.down_attempted:
                    Square.history.append(element + [(x + 1, y)])
                    current_pos.down_attempted = True
                if current_pos.left_accessible and not current_pos.left_attempted:
                    Square.history.append(element + [(x, y - 1)])
                    current_pos.left_attempted = True
                if current_pos.right_accessible and not current_pos.right_attempted:
                    Square.history.append(element + [(x, y + 1)])
                    current_pos.right_attempted = True

        solution_lengths = []
        for solution in Square.history:
            solution_lengths.append(len(solution))
        return min(solution_lengths) - 1

    def __init__(self, x, y, letter_height) -> None:
        self.x_pos = x
        self.y_pos = y
        self.height = ord(letter_height) - 96
        self.up_accessible = None
        self.down_accessible = None
        self.left_accessible = None
        self.right_accessible = None
        self.up_attempted = False
        self.down_attempted = False
        self.left_attempted = False
        self.right_attempted = False
        self.is_start = False
        self.is_finish = False
        if letter_height == "S":
            self.set_as_start()
            Square.history.append([(x, y)])
        elif letter_height == "E":
            self.set_as_finish()

    def __str__(self) -> str:
        return f"""        Coordinates: ({self.x_pos}, {self.y_pos})
        Height: {self.height}
        Can go up: {self.up_accessible}
        Can go down: {self.down_accessible}
        Can go left: {self.left_accessible}
        Can go right: {self.right_accessible}
        Is starting position: {self.is_start}
        Is finishing position: {self.is_finish}"""

    def determine_up(self):
        if self.x_pos == 0:
            self.up_accessible = False
            return
        up = Square.grid[self.x_pos - 1][self.y_pos]
        if up.is_start:
            self.up_accessible = False
        elif up.height <= self.height + 1:
            self.up_accessible = True
        else:
            self.up_accessible = False

    def determine_down(self):
        if self.x_pos == Square.GRID_HEIGHT - 1:
            self.down_accessible = False
            return
        down = Square.grid[self.x_pos + 1][self.y_pos]
        if down.is_start:
            self.down_accessible = False
        elif down.height <= self.height + 1:
            self.down_accessible = True
        else:
            self.down_accessible = False

    def determine_left(self):
        if self.y_pos == 0:
            self.left_accessible = False
            return
        left = Square.grid[self.x_pos][self.y_pos - 1]
        if left.is_start:
            self.left_accessible = False
        elif left.height <= self.height + 1:
            self.left_accessible = True
        else:
            self.left_accessible = False

    def determine_right(self):
        if self.y_pos == Square.GRID_WIDTH - 1:
            self.right_accessible = False
            return
        right = Square.grid[self.x_pos][self.y_pos + 1]
        if right.is_start:
            self.right_accessible = False
        elif right.height <= self.height + 1:
            self.right_accessible = True
        else:
            self.right_accessible = False

    def determine_possible_moves(self):
        if self.is_finish:
            self.up_accessible = False
            self.down_accessible = False
            self.right_accessible = False
            self.left_accessible = False
        else:
            self.determine_up()
            self.determine_down()
            self.determine_left()
            self.determine_right()

    def set_as_start(self):
        self.is_start = True
        self.height = 1

    def set_as_finish(self):
        self.is_finish = True
        self.height = 27

    def is_stuck(self):
        return (
            ((not self.up_accessible) or self.up_attempted)
            and ((not self.down_accessible) or self.down_attempted)
            and ((not self.right_accessible) or self.right_attempted)
            and ((not self.left_accessible) or self.left_attempted)
        )


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Square.convert_to_grid(content)
    Square.determine_all_possible_moves()
    print(Square.find_path_to_finish())
