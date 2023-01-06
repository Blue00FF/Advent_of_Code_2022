import numpy as np
import abc


class Block:
    grid = []
    GRID_WIDTH = 7
    GRID_HEIGHT = 3200

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

    def start_falling_rocks_part_1(n_pieces=2022):
        Piece.tower_top = 0
        i = 0
        period_length = 5 * len(Piece.wind_directions)
        previous_period = 0
        current_period = 0
        for n in range(n_pieces):
            if n % period_length == 0:
                current_period = Piece.tower_top
                print(f"{n} : {current_period - previous_period}")
                previous_period = current_period
            current_piece = Piece.piece_dispenser(n)
            while current_piece.is_falling():
                next_direction = Piece.direction_dispenser(i)
                i += 1
                current_piece.push(next_direction)
                current_piece.fall()

    def start_falling_rocks_part_2(n_pieces=1000000000000):
        Piece.tower_top = 0
        i = 0
        period_length = 5 * len(Piece.wind_directions)
        for n in range(period_length):
            current_piece = Piece.piece_dispenser(n)
            while current_piece.is_falling():
                next_direction = Piece.direction_dispenser(i)
                i += 1
                current_piece.push(next_direction)
                current_piece.fall()
        periodic_height = float(Piece.tower_top)
        for n in range(n_pieces % period_length):
            current_piece = Piece.piece_dispenser(n)
            while current_piece.is_falling():
                next_direction = Piece.direction_dispenser(i)
                i += 1
                current_piece.push(next_direction)
                current_piece.fall()
        Piece.tower_top += periodic_height * (n_pieces // period_length - 1)

    def start_test_falling_rocks(n_pieces=1000000000000):
        pattern = {0: 300, 1: 306, 2: 303, 3: 303, 4: 301, 5: 306, 6: 301}
        Piece.tower_top = 308
        period_length = 5 * len(Piece.wind_directions)
        n_pieces -= period_length
        number_of_periods = n_pieces // period_length
        number_of_complete_cycles = number_of_periods // 7
        Piece.tower_top += number_of_complete_cycles * (
            300 + 306 + 303 + 303 + 301 + 306 + 301
        )
        number_of_residual_periods = number_of_periods % 7
        for n in range(number_of_residual_periods):
            Piece.tower_top += pattern[n]
        tower_top_storage = Piece.tower_top
        Piece.tower_top = 0
        Piece.start_falling_rocks_part_1(number_of_residual_periods + 1)
        tower_top_diff = Piece.tower_top
        Piece.start_falling_rocks_part_1(n_pieces % period_length)
        tower_top_diff = Piece.tower_top - tower_top_diff
        return tower_top_storage + tower_top_diff

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
    Block.GRID_HEIGHT = 10000000
    Piece.process_input(content)
    Block.generate_grid()
    Piece.start_falling_rocks_part_1(1000000000000)
    print(Piece.tower_top)
    # Block.generate_grid()
    # Piece.start_falling_rocks_part_2()
    # print(Piece.tower_top)


pattern = {
    50455: 79263,
    100910: 79241,
    151365: 79218,
    201820: 79237,
    252275: 79250,
    302730: 79240,
    353185: 79220,
    403640: 79236,
    454095: 79250,
    504550: 79236,
    555005: 79226,
    605460: 79234,
    655915: 79250,
    706370: 79232,
    756825: 79227,
    807280: 79237,
    857735: 79248,
    908190: 79230,
    958645: 79230,
    1009100: 79238,
    1059555: 79249,
    1110010: 79226,
    1160465: 79233,
    1210920: 79238,
    1261375: 79248,
    1311830: 79225,
    1362285: 79231,
    1412740: 79242,
    1463195: 79242,
    1513650: 79232,
    1564105: 79228,
    1614560: 79244,
    1665015: 79241,
    1715470: 79233,
    1765925: 79227,
    1816380: 79246,
    1866835: 79238,
    1917290: 79234,
    1967745: 79228,
    2018200: 79246,
    2068655: 79236,
    2119110: 79235,
    2169565: 79229,
    2220020: 79244,
    2270475: 79235,
    2320930: 79236,
    2371385: 79233,
    2421840: 79240,
    2472295: 79233,
    2522750: 79240,
    2573205: 79234,
    2623660: 79235,
    2674115: 79232,
    2724570: 79245,
    2775025: 79234,
    2825480: 79233,
    2875935: 79230,
    2926390: 79250,
    2976845: 79232,
    3027300: 79233,
    3077755: 79227,
    3128210: 79250,
    3178665: 79239,
    3229120: 79231,
    3279575: 79223,
    3330030: 79248,
    3380485: 79242,
    3430940: 79230,
    3481395: 79222,
    3531850: 79251,
    3582305: 79245,
    3632760: 79231,
    3683215: 79218,
    3733670: 79247,
    3784125: 79250,
    3834580: 79231,
    3885035: 79217,
    3935490: 79248,
    3985945: 79254,
    4036400: 79227,
    4086855: 79220,
    4137310: 79243,
    4187765: 79253,
    4238220: 79230,
    4288675: 79217,
    4339130: 79247,
    4389585: 79252,
    4440040: 79233,
    4490495: 79215,
    4540950: 79247,
    4591405: 79253,
    4641860: 79232,
    4692315: 79213,
    4742770: 79251,
    4793225: 79247,
    4843680: 79233,
    4894135: 79212,
    4944590: 79252,
    4995045: 79248,
    5045500: 79232,
    5095955: 79217,
    5146410: 79251,
    5196865: 79243,
    5247320: 79233,
    5297775: 79217,
    5348230: 79250,
    5398685: 79242,
    5449140: 79235,
    5499595: 79218,
    5550050: 79250,
    5600505: 79244,
    5650960: 79233,
    5701415: 79217,
    5751870: 79255,
    5802325: 79242,
    5852780: 79234,
    5903235: 79216,
    5953690: 79250,
    6004145: 79249,
    6054600: 79231,
    6105055: 79216,
    6155510: 79250,
    6205965: 79247,
    6256420: 79233,
    6306875: 79214,
    6357330: 79250,
}
