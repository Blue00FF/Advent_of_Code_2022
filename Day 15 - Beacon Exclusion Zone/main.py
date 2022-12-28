class Sensor:
    grid = []
    sensors = []
    GRID_HEIGHT = 0
    GRID_WIDTH = 0

    def generate_grid():
        for x in range(Sensor.GRID_HEIGHT):
            Sensor.grid.append([])
            for y in range(Sensor.GRID_WIDTH):
                Sensor.grid[x].append([])

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
            if max(x_sensor, x_beacon) > Sensor.GRID_HEIGHT - 1:
                Sensor.GRID_HEIGHT = max(x_sensor, x_beacon) + 1
            if max(y_sensor, y_beacon) > Sensor.GRID_WIDTH - 1:
                Sensor.GRID_WIDTH = max(y_sensor, y_beacon) + 1

    def __init__(self, x, y, x_beacon, y_beacon) -> None:
        self.x = x
        self.y = y
        self.x_beacon = x_beacon
        self.y_beacon = y_beacon

    def __str__(self) -> str:
        return (
            f"Sensor coordinate x: {self.y}"
            f"\nSensor coordinate y: {self.x}"
            f"\nBeacon coordinate x: {self.y_beacon}"
            f"\nBeacon coordinate y: {self.x_beacon}"
        )


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Sensor.process_input(content)
