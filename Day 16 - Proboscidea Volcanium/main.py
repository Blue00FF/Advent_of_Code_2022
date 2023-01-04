import numpy as np


class Valve:
    valves = {}
    useful_valves = []
    complete_paths = []
    max_released_pressure = 0

    def process_input(content):
        split_input = content.split("\n")
        for line in split_input:
            Valve(line)

    def start_part_1():
        Valve.find_all_possible_paths()
        Valve.max_released_pressure = 0
        for path in Valve.complete_paths:
            current_flow = 0
            released_pressure = 0
            for i in range(1, len(path)):
                path_length = path[i - 1].find_path_length(path[i])
                released_pressure += current_flow * path_length
                current_flow += path[i].flow_rate
            if released_pressure > Valve.max_released_pressure:
                Valve.max_released_pressure = released_pressure

    def advance_level(current_level):
        next_level_labels = []
        next_level = []
        for valve in current_level:
            next_level_labels += valve.valves_connected
        next_level_labels = list(set(next_level_labels))
        for label in next_level_labels:
            next_level.append(Valve.valves[label])
        return next_level

    def find_all_possible_paths():
        current_valve = Valve.valves["AA"]
        incomplete_paths = [[x] for x in Valve.useful_valves]
        paths_time_spent = {}
        Valve.complete_paths = []
        for index in range(len(incomplete_paths)):
            incomplete_paths[index] = [current_valve] + incomplete_paths[index]
            paths_time_spent.update(
                {
                    Valve.path_to_string(
                        incomplete_paths[index]
                    ): current_valve.find_path_length(incomplete_paths[index][1])
                    + 1
                }
            )
        while len(incomplete_paths) > 0:
            temp_incomplete_paths = incomplete_paths.copy()
            incomplete_paths = []
            for path_index in range(len(temp_incomplete_paths)):
                current_valve = temp_incomplete_paths[path_index][-1]
                next_steps = Valve.useful_valves.copy()
                for step in next_steps:
                    if step not in temp_incomplete_paths[path_index]:
                        time_spent = (
                            paths_time_spent[
                                Valve.path_to_string(temp_incomplete_paths[path_index])
                            ]
                            + current_valve.find_path_length(step)
                            + 1
                        )

                        if time_spent < 30:
                            incomplete_paths.append(
                                temp_incomplete_paths[path_index] + [step]
                            )
                            paths_time_spent.update(
                                {
                                    Valve.path_to_string(
                                        temp_incomplete_paths[path_index] + [step]
                                    ): time_spent
                                }
                            )
                        elif time_spent == 30:
                            Valve.complete_paths.append(
                                temp_incomplete_paths[path_index] + [step]
                            )
                        elif (
                            temp_incomplete_paths[path_index]
                            not in Valve.complete_paths
                        ):
                            Valve.complete_paths.append(
                                temp_incomplete_paths[path_index]
                            )

    def path_to_string(path):
        result = ""
        for valve in path:
            result += valve.valve_label
        return result

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

    def find_path_length(self, next_valve):
        if self == next_valve:
            return 0
        possible_paths = [[x] for x in Valve.advance_level([self])]
        while True:
            temp_possible_paths = possible_paths.copy()
            possible_paths = []
            for path_index in range(len(temp_possible_paths)):
                current_valve = temp_possible_paths[path_index][-1]
                if current_valve == next_valve:
                    return len(temp_possible_paths[path_index])
                next_steps = Valve.advance_level([current_valve])
                for step in next_steps:
                    possible_paths.append(temp_possible_paths[path_index] + [step])


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Valve.process_input(content)
    Valve.start_part_1()
    print(Valve.max_released_pressure)
