class Valve:
    valves = {}
    useful_valves = []
    current_flow = 0
    time_remaining = 30
    released_pressure = 0

    def flow():
        Valve.released_pressure += Valve.current_flow
        Valve.time_remaining -= 1

    def move_to_valve(valve_label):
        Valve.flow()
        return Valve.valves[valve_label]

    def process_input(content):
        split_input = content.split("\n")
        for line in split_input:
            Valve(line)

    def start_part_1():
        current_valve = Valve.valves["AA"]
        while Valve.time_remaining > 0:
            next_valve = current_valve.find_next_best_valve()
            if next_valve:
                path_to_next = current_valve.find_path(next_valve)
                for step in path_to_next:
                    current_valve = Valve.move_to_valve(step.valve_label)
                current_valve.open()
            else:
                Valve.flow()

    def iterate_flow_rates(current_level):
        current_level_flow_rates = []
        for valve in current_level:
            if not valve.is_open:
                current_level_flow_rates.append(valve.flow_rate)
        return current_level_flow_rates

    def advance_level(current_level):
        next_level_labels = []
        next_level = []
        for valve in current_level:
            next_level_labels += valve.valves_connected
        next_level_labels = list(set(next_level_labels))
        for label in next_level_labels:
            next_level.append(Valve.valves[label])
        return next_level

    def __init__(self, line) -> None:
        valve_info = line.split()
        self.valve_label = valve_info[1]
        self.flow_rate = int(valve_info[4].split("=")[1][:-1])
        self.valves_connected = valve_info[9:]
        for index in range(len(self.valves_connected) - 1):
            self.valves_connected[index] = self.valves_connected[index][:-1]
        self.is_open = False
        Valve.valves.update({self.valve_label: self})
        if self.flow_rate > 0:
            Valve.useful_valves.append(self)

    def __str__(self) -> str:
        return (
            f"Valve {self.valve_label} has"
            f" flow rate={self.flow_rate};"
            f" tunnels lead to valves {self.valves_connected}"
            f" and is open? {self.is_open}"
        )

    def __eq__(self, o: object) -> bool:
        return self.valve_label == o.valve_label

    def open(self):
        if self.is_open:
            raise Exception("Valve is already open!")
        Valve.flow()
        self.is_open = True
        Valve.current_flow += self.flow_rate

    def find_next_best_valve(self):
        champion_valve = None
        max_score = 0
        for valve in Valve.useful_valves:
            valve_score = valve.flow_rate * (
                Valve.time_remaining - len(self.find_path(valve)) - 1
            )
            if valve_score > max_score:
                max_score = valve_score
                champion_valve = valve
        if champion_valve:
            Valve.useful_valves.remove(champion_valve)
            print(champion_valve.valve_label)
        return champion_valve

    def find_path(self, next_valve):
        if self == next_valve:
            return []
        possible_paths = [[x] for x in Valve.advance_level([self])]
        while True:
            temp_possible_paths = possible_paths.copy()
            possible_paths = []
            for path_index in range(len(temp_possible_paths)):
                current_valve = temp_possible_paths[path_index][-1]
                if current_valve == next_valve:
                    return temp_possible_paths[path_index]
                next_steps = Valve.advance_level([current_valve])
                for step in next_steps:
                    possible_paths.append(temp_possible_paths[path_index] + [step])


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Valve.process_input(content)
    Valve.start_part_1()
    print(Valve.released_pressure)
