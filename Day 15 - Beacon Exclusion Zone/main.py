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
            Sensor.sensor_positions.append((x_sensor, y_sensor))
            Sensor.beacon_positions.append((x_beacon, y_beacon))

    def lay_out_sensors(x_position):
        for sensor in Sensor.sensors:
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

    def part_1_set_up(content, x_position):
        Sensor.process_input(content)
        Sensor.lay_out_sensors(x_position)

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
    Sensor.initial_set_up(content, 2000000)
    print(Sensor.count_detected_positions(2000000))
