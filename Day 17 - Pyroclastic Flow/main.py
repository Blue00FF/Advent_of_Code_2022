import numpy as np
import abc


class Block:
    grid = []
    GRID_WIDTH = 7
    GRID_HEIGHT = 4000

    def generate_grid():
        grid = []
        grid.append([])
        for _ in range(Block.GRID_WIDTH + 2):
            grid[0].append(Block("rock"))
        for y in range(1, Block.GRID_HEIGHT):
            grid.append([])
            grid[y].append(Block("rock"))
            for _ in range(Block.GRID_WIDTH):
                grid[y].append(Block("air"))
            grid[y].append(Block("rock"))
        Block.grid = grid

    def visualise_grid():
        for y in range(Block.GRID_HEIGHT - 1, 0, -1):
            print("|", sep="", end="")
            for x in range(1, Block.GRID_WIDTH + 1):
                current_block = Block.get_grid_coord(x, y)
                if current_block.is_rock():
                    print("#", sep="", end="")
                else:
                    print(".", sep="", end="")
            print("|", sep="", end="")
            print()
        print("+", sep="", end="")
        for x in range(1, Block.GRID_WIDTH + 1):
            print("-", sep="", end="")
        print("+", sep="", end="")
        print()

    def get_grid_coord(x, y):
        return Block.grid[y][x]

    def __init__(self, block_type) -> None:
        self.block_type = block_type

    def is_rock(self):
        return self.block_type == "rock"

    def turn_into_rock(self):
        self.block_type = "rock"


class Piece(abc.ABC):
    tower_top = 0
    wind_directions = []

    def process_input(content):
        Piece.wind_directions = list(content)

    def start_part_1(n_pieces=2022):
        i = 0
        for n in range(n_pieces):
            current_piece = Piece.piece_dispenser(n)
            while current_piece.is_falling():
                next_direction = Piece.direction_dispenser(i)
                i += 1
                current_piece.push(next_direction)
                current_piece.fall()

    def piece_dispenser(n):
        piece_dict = {
            0: Bar_Piece(),
            1: Plus_Piece(),
            2: L_Piece(),
            3: Pipe_Piece(),
            4: Square_Piece(),
        }
        return piece_dict[n % 5]

    def direction_dispenser(i):
        return Piece.wind_directions[i % len(Piece.wind_directions)]

    @abc.abstractmethod
    def __init__(self) -> None:
        self.piece_positions = []
        self.falling = True

    def __str__(self) -> str:
        result = f"The piece blocks are at positions "
        for position in self.piece_positions:
            result += f"({position[0]}, {position[1]}), "
        return result

    def is_falling(self):
        return self.falling

    def move(self, index, delta):
        for piece_position in self.piece_positions:
            piece_position[index] += delta

    def fall(self):
        if not self.falling:
            raise Exception("Block is at rest!")
        if self.unable_to_fall():
            self.stop_falling()
        else:
            self.move(1, -1)

    def stop_falling(self):
        self.falling = False
        top_piece_position = 0
        for piece_position in self.piece_positions:
            x, y = piece_position[0], piece_position[1]
            Block.get_grid_coord(x, y).turn_into_rock()
            if y > top_piece_position:
                top_piece_position = y
        if top_piece_position > Piece.tower_top:
            Piece.tower_top = top_piece_position

    def push(self, direction):
        if direction == "<":
            self.push_left()
        elif direction == ">":
            self.push_right()
        else:
            raise Exception("Invalid direction!")

    def push_left(self):
        if self.unable_to_left():
            pass
        else:
            self.move(0, -1)

    def push_right(self):
        if self.unable_to_right():
            pass
        else:
            self.move(0, 1)

    def unable_to_fall(self):
        for position in self.piece_positions:
            x, y = position[0], position[1]
            if Block.get_grid_coord(x, y - 1).is_rock():
                return True
        return False

    def unable_to_left(self):
        for position in self.piece_positions:
            x, y = position[0], position[1]
            if Block.get_grid_coord(x - 1, y).is_rock():
                return True
        return False

    def unable_to_right(self):
        for position in self.piece_positions:
            x, y = position[0], position[1]
            if Block.get_grid_coord(x + 1, y).is_rock():
                return True
        return False


class Bar_Piece(Piece):
    def __init__(self) -> None:
        super().__init__()
        leftmost = 3
        bottom = Piece.tower_top + 4
        self.piece_positions = [
            np.array([leftmost, bottom]),
            np.array([leftmost + 1, bottom]),
            np.array([leftmost + 2, bottom]),
            np.array([leftmost + 3, bottom]),
        ]


class Plus_Piece(Piece):
    def __init__(self) -> None:
        super().__init__()
        leftmost = 3
        bottom = Piece.tower_top + 4
        self.piece_positions = [
            np.array([leftmost, bottom + 1]),
            np.array([leftmost + 1, bottom]),
            np.array([leftmost + 1, bottom + 1]),
            np.array([leftmost + 2, bottom + 1]),
            np.array([leftmost + 1, bottom + 2]),
        ]


class L_Piece(Piece):
    def __init__(self) -> None:
        super().__init__()
        leftmost = 3
        bottom = Piece.tower_top + 4
        self.piece_positions = [
            np.array([leftmost, bottom]),
            np.array([leftmost + 1, bottom]),
            np.array([leftmost + 2, bottom]),
            np.array([leftmost + 2, bottom + 1]),
            np.array([leftmost + 2, bottom + 2]),
        ]


class Pipe_Piece(Piece):
    def __init__(self) -> None:
        super().__init__()
        leftmost = 3
        bottom = Piece.tower_top + 4
        self.piece_positions = [
            np.array([leftmost, bottom]),
            np.array([leftmost, bottom + 1]),
            np.array([leftmost, bottom + 2]),
            np.array([leftmost, bottom + 3]),
        ]


class Square_Piece(Piece):
    def __init__(self) -> None:
        super().__init__()
        leftmost = 3
        bottom = Piece.tower_top + 4
        self.piece_positions = [
            np.array([leftmost, bottom]),
            np.array([leftmost + 1, bottom]),
            np.array([leftmost, bottom + 1]),
            np.array([leftmost + 1, bottom + 1]),
        ]


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Piece.process_input(content)
    Block.generate_grid()
    Piece.start_part_1()
    print(Piece.tower_top)
