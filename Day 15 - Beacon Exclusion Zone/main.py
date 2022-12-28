def manhattan_distance(x_1, y_1, x_2, y_2):
    x_dist = abs(x_1 - x_2)
    y_dist = abs(y_1 - y_2)
    return x_dist + y_dist


class Block:
    def __init__(self, block_type) -> None:
        self.type = block_type
        self.detected = False

    def turn_into_sensor(self):
        self.type = "sensor"
        self.detected = True

    def turn_into_beacon(self):
        self.type = "beacon"
        self.detected = True

    def turn_into_ground(self):
        self.type = "ground"
        self.detected = False

    def detect(self):
        self.detected = True

    def is_detected(self):
        return self.detected

    def is_beacon(self):
        return self.type == "beacon"


class Sensor:
    grid = []
    sensors = []
    X_MIN = float("inf")
    X_MAX = float("-inf")
    GRID_HEIGHT = 0
    Y_MIN = float("inf")
    Y_MAX = float("-inf")
    GRID_WIDTH = 0

    def generate_grid():
        for x in range(Sensor.GRID_HEIGHT):
            Sensor.grid.append([])
            for _ in range(Sensor.GRID_WIDTH):
                Sensor.grid[x].append(Block("ground"))

    def select_grid(x, y):
        return Sensor.grid[x - Sensor.X_MIN][y - Sensor.Y_MIN]

    def process_input(content):
        split_content = content.split("\n")
        for line in split_content:
            y_beacon, x_beacon = line.split()[-2][:-1], line.split()[-1]
            x_beacon = int(x_beacon.split("=")[1])
            y_beacon = int(y_beacon.split("=")[1])
            y_sensor, x_sensor = line.split()[2][:-1], line.split()[3][:-1]
            x_sensor = int(x_sensor.split("=")[1])
            y_sensor = int(y_sensor.split("=")[1])
            Sensor.sensors.append(Sensor(x_sensor, y_sensor, x_beacon, y_beacon))
            if max(x_sensor, x_beacon) > Sensor.X_MAX:
                Sensor.X_MAX = max(x_sensor, x_beacon)
            if max(y_sensor, y_beacon) > Sensor.Y_MAX:
                Sensor.Y_MAX = max(y_sensor, y_beacon)
            if min(x_sensor, x_beacon) < Sensor.X_MIN:
                Sensor.X_MIN = min(x_sensor, x_beacon)
            if min(y_sensor, y_beacon) < Sensor.Y_MIN:
                Sensor.Y_MIN = min(y_sensor, y_beacon)
        Sensor.GRID_HEIGHT = Sensor.X_MAX - Sensor.X_MIN + 1
        Sensor.GRID_WIDTH = Sensor.Y_MAX - Sensor.Y_MIN + 1

    def lay_out_sensors():
        for sensor in Sensor.sensors:
            Sensor.select_grid(sensor.x, sensor.y).turn_into_sensor()
            Sensor.select_grid(sensor.x_beacon, sensor.y_beacon).turn_into_beacon()
            min_x = max(sensor.x - sensor.detection_distance, Sensor.X_MIN)
            min_y = max(sensor.y - sensor.detection_distance, Sensor.Y_MIN)
            max_x = min(sensor.x + sensor.detection_distance, Sensor.X_MAX)
            max_y = min(sensor.y + sensor.detection_distance, Sensor.Y_MAX)
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if (
                        manhattan_distance(sensor.x, sensor.y, x, y)
                        <= sensor.detection_distance
                    ):
                        Sensor.select_grid(x, y).detect()

    def initial_set_up(content):
        Sensor.process_input(content)
        Sensor.generate_grid()
        Sensor.lay_out_sensors()

    def visualise_grid():
        x = Sensor.X_MIN
        for line in Sensor.grid:
            print(x, end="", sep="")
            for square in line:
                if square.type == "sensor":
                    print("S", end="", sep="")
                elif square.type == "beacon":
                    print("B", end="", sep="")
                elif square.is_detected():
                    print("#", end="", sep="")
                else:
                    print(".", end="", sep="")
            print()
            x += 1

    def calculate_detected_positions(line_index):
        line = Sensor.grid[line_index - Sensor.X_MIN]
        detected_counter = 0
        for square in line:
            if (not square.is_beacon()) and square.is_detected():
                detected_counter += 1
        return detected_counter

    def __init__(self, x, y, x_beacon, y_beacon) -> None:
        self.x = x
        self.y = y
        self.x_beacon = x_beacon
        self.y_beacon = y_beacon
        self.detection_distance = self.beacon_distance()

    def __str__(self) -> str:
        return (
            f"Sensor coordinate x: {self.y}"
            f"\nSensor coordinate y: {self.x}"
            f"\nBeacon coordinate x: {self.y_beacon}"
            f"\nBeacon coordinate y: {self.x_beacon}"
        )

    def beacon_distance(self):
        return manhattan_distance(self.x, self.y, self.x_beacon, self.y_beacon)


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Sensor.initial_set_up(content)
    print(Sensor.calculate_detected_positions(2000000))
