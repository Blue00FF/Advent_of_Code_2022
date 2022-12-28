def manhattan_distance(x_1, y_1, x_2, y_2):
    x_dist = abs(x_1 - x_2)
    y_dist = abs(y_1 - y_2)
    return x_dist + y_dist


class Sensor:
    grid = []
    sensors = []
    sensor_positions = []
    beacon_positions = []
    detected_positions = []
    MAX_COORD = 0

    def process_input_part_1(content):
        split_content = content.split("\n")
        for line in split_content:
            y_beacon, x_beacon = line.split()[-2][:-1], line.split()[-1]
            x_beacon = int(x_beacon.split("=")[1])
            y_beacon = int(y_beacon.split("=")[1])
            y_sensor, x_sensor = line.split()[2][:-1], line.split()[3][:-1]
            x_sensor = int(x_sensor.split("=")[1])
            y_sensor = int(y_sensor.split("=")[1])
            Sensor.sensors.append(Sensor(x_sensor, y_sensor, x_beacon, y_beacon))
            Sensor.sensor_positions.append((x_sensor, y_sensor))
            Sensor.beacon_positions.append((x_beacon, y_beacon))

    def process_input_part_2(content):
        split_content = content.split("\n")
        Sensor.sensors = []
        Sensor.sensor_positions = []
        Sensor.beacon_positions = []
        Sensor.detected_positions = []
        for line in split_content:
            y_beacon, x_beacon = line.split()[-2][:-1], line.split()[-1]
            x_beacon = int(x_beacon.split("=")[1])
            y_beacon = int(y_beacon.split("=")[1])
            y_sensor, x_sensor = line.split()[2][:-1], line.split()[3][:-1]
            x_sensor = int(x_sensor.split("=")[1])
            y_sensor = int(y_sensor.split("=")[1])
            Sensor.sensors.append(Sensor(x_sensor, y_sensor, x_beacon, y_beacon))
            if 0 <= x_sensor <= Sensor.MAX_COORD and 0 <= y_sensor <= Sensor.MAX_COORD:
                Sensor.sensor_positions.append((x_sensor, y_sensor))
            if 0 <= x_beacon <= Sensor.MAX_COORD and 0 <= y_beacon <= Sensor.MAX_COORD:
                Sensor.beacon_positions.append((x_beacon, y_beacon))
        Sensor.beacon_positions = set(Sensor.beacon_positions)

    def process_part_1(x_position):
        for sensor_index, sensor in enumerate(Sensor.sensors):
            print(f"{round(sensor_index/28*100,0)} % done")
            min_y = sensor.y - sensor.detection_distance
            max_y = sensor.y + sensor.detection_distance
            x = x_position
            for y in range(min_y, max_y + 1):
                if (
                    ((x, y) not in Sensor.sensor_positions)
                    and ((x, y) not in Sensor.beacon_positions)
                    and manhattan_distance(sensor.x, sensor.y, x, y)
                    <= sensor.detection_distance
                ):
                    Sensor.detected_positions.append((x, y))
        Sensor.detected_positions = set(Sensor.detected_positions)

    def process_part_2():
        for x in range(Sensor.MAX_COORD + 1):
            for y in range(Sensor.MAX_COORD + 1):
                Sensor.grid.append((x, y))
        for position in Sensor.sensor_positions:
            Sensor.grid.remove(position)
        for position in Sensor.beacon_positions:
            Sensor.grid.remove(position)
        for sensor_index, sensor in enumerate(Sensor.sensors):
            print(f"{round(sensor_index/28*100,0)} % done")
            min_y = max(sensor.y - sensor.detection_distance, 0)
            max_y = min(sensor.y + sensor.detection_distance, Sensor.MAX_COORD)
            min_x = max(sensor.x - sensor.detection_distance, 0)
            max_x = min(sensor.x + sensor.detection_distance, Sensor.MAX_COORD)
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if (
                        ((x, y) not in Sensor.sensor_positions)
                        and ((x, y) not in Sensor.beacon_positions)
                        and manhattan_distance(sensor.x, sensor.y, x, y)
                        <= sensor.detection_distance
                    ):
                        Sensor.detected_positions.append((x, y))
        Sensor.detected_positions = set(Sensor.detected_positions)
        for position in Sensor.detected_positions:
            Sensor.grid.remove(position)

    def part_1_set_up(content, x_position):
        Sensor.process_input_part_1(content)
        Sensor.process_part_1(x_position)

    def part_2_set_up(content):
        Sensor.process_input_part_2(content)
        Sensor.process_part_2()

    def count_detected_positions(x_index):
        detected_counter = 0
        for position in Sensor.detected_positions:
            if position[0] == x_index:
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
    # Sensor.part_1_set_up(content, 2000000)
    # print(Sensor.count_detected_positions(2000000))
    Sensor.MAX_COORD = 4000000
    Sensor.part_2_set_up(content)
    print(Sensor.grid)
