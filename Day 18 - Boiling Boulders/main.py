class Cube:
    grid = []
    cube_positions = []
    GRID_SIZE = 0

    def generate_grid():
        grid = []
        for x in range(Cube.GRID_SIZE):
            grid.append([])
            for y in range(Cube.GRID_SIZE):
                grid[x].append([])
                for z in range(Cube.GRID_SIZE):
                    grid[x][y].append(Cube(x, y, z, "void"))
        Cube.grid = grid

    def process_input(content):
        cube_positions = []
        for line in content.split("\n"):
            x, y, z = map(int, line.split(","))
            Cube.grid[x][y][z].turn_into_lava()
            cube_positions.append((x, y, z))
        Cube.cube_positions = cube_positions

    def calculate_total_surface_area():
        total_surface_area = 0
        for position in Cube.cube_positions:
            total_surface_area += Cube.get_grid_position(*position).surface_area
        return total_surface_area

    def calculate_total_external_surface_area():
        total_external_surface_area = 0
        for position in Cube.cube_positions:
            total_external_surface_area += Cube.get_grid_position(
                *position
            ).external_surface_area
        return total_external_surface_area

    def get_grid_position(x, y, z):
        return Cube.grid[x][y][z]

    def calculate_surface_areas():
        for position in Cube.cube_positions:
            Cube.get_grid_position(*position).calculate_surface_area()

    def calculate_external_surface_areas():
        Cube.start_air_floodfill()
        for position in Cube.cube_positions:
            Cube.get_grid_position(*position).calculate_external_surface_area()

    def start_air_floodfill():
        current_pos = Cube.get_grid_position(
            Cube.GRID_SIZE - 1, Cube.GRID_SIZE - 1, Cube.GRID_SIZE - 1
        )
        neighbours = current_pos.get_neighbours()
        while len(neighbours) > 0:
            next_neighbours = []
            for neighbour in neighbours:
                neighbour.turn_into_air()
                next_neighbours += neighbour.get_neighbours()
            next_neighbours = list(set(next_neighbours))
            neighbours = next_neighbours.copy()

    def __init__(self, x, y, z, cube_type) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.cube_type = cube_type
        self.surface_area = 0
        self.external_surface_area = 0
        self.checked = False

    def turn_into_lava(self):
        self.cube_type = "lava"

    def turn_into_air(self):
        self.cube_type = "air"

    def is_lava(self):
        return self.cube_type == "lava"

    def is_air(self):
        return self.cube_type == "air"

    def is_void(self):
        return self.cube_type == "void"

    def get_neighbours(self):
        neighbours = []
        for i in (-1, +1):
            if (
                self.x + i < Cube.GRID_SIZE
                and self.x >= 0
                and Cube.get_grid_position(self.x + i, self.y, self.z).is_void()
            ):
                neighbours.append(Cube.get_grid_position(self.x + i, self.y, self.z))
            if (
                self.y + i < Cube.GRID_SIZE
                and self.y >= 0
                and Cube.get_grid_position(self.x, self.y + i, self.z).is_void()
            ):
                neighbours.append(Cube.get_grid_position(self.x, self.y + i, self.z))
            if (
                self.z + i < Cube.GRID_SIZE
                and self.z >= 0
                and Cube.get_grid_position(self.x, self.y, self.z + i).is_void()
            ):
                neighbours.append(Cube.get_grid_position(self.x, self.y, self.z + i))
        return neighbours

    def calculate_surface_area(self):
        surface_area = 0
        for i in (-1, +1):
            if Cube.get_grid_position(self.x + i, self.y, self.z).is_void():
                surface_area += 1
            if Cube.get_grid_position(self.x, self.y + i, self.z).is_void():
                surface_area += 1
            if Cube.get_grid_position(self.x, self.y, self.z + i).is_void():
                surface_area += 1
        self.surface_area = surface_area

    def calculate_external_surface_area(self):
        surface_area = 0
        for i in (-1, +1):
            if Cube.get_grid_position(self.x + i, self.y, self.z).is_air():
                surface_area += 1
            if Cube.get_grid_position(self.x, self.y + i, self.z).is_air():
                surface_area += 1
            if Cube.get_grid_position(self.x, self.y, self.z + i).is_air():
                surface_area += 1
        self.external_surface_area = surface_area


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Cube.GRID_SIZE = 30
    Cube.generate_grid()
    Cube.process_input(content)
    Cube.calculate_surface_areas()
    print(Cube.calculate_total_surface_area())
    Cube.calculate_external_surface_areas()
    print(Cube.calculate_total_external_surface_area())
