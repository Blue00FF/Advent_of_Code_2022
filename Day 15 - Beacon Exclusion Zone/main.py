def manhattan_distance(x_1, y_1, x_2, y_2):
    x_dist = abs(x_1 - x_2)
    y_dist = abs(y_1 - y_2)
    return x_dist + y_dist


class Sensor:
    grid = []
    sensors = []
    sensor_positions = []
    beacon_positions = []
    MAX_COORD = 0
    X_MIN = float("inf")
    X_MAX = float("-inf")
    Y_MIN = float("inf")
    Y_MAX = float("-inf")

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
        for sensor in Sensor.sensors:
            if sensor.x + sensor.detection_distance > Sensor.X_MAX:
                Sensor.X_MAX = sensor.x + sensor.detection_distance
            if sensor.y + sensor.detection_distance > Sensor.Y_MAX:
                Sensor.Y_MAX = sensor.y + sensor.detection_distance
            if sensor.x - sensor.detection_distance < Sensor.X_MIN:
                Sensor.X_MIN = sensor.x - sensor.detection_distance
            if sensor.y - sensor.detection_distance < Sensor.Y_MIN:
                Sensor.Y_MIN = sensor.y - sensor.detection_distance

    def check_exclusion(x, y):
        for sensor in Sensor.sensors:
            if (
                manhattan_distance(sensor.x, sensor.y, x, y)
                <= sensor.detection_distance
            ):
                return True
        return False

    def count_excluded_squares(x_position):
        exclusion_counter = 0
        x = x_position
        for y in range(Sensor.Y_MIN, Sensor.Y_MAX + 1):
            if (
                ((x, y) not in Sensor.sensor_positions)
                and ((x, y) not in Sensor.beacon_positions)
                and Sensor.check_exclusion(x, y)
            ):
                exclusion_counter += 1
        return exclusion_counter

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
    Sensor.process_input(content)
    print(Sensor.count_excluded_squares(2000000))
    # Sensor.MAX_COORD = 4000000
