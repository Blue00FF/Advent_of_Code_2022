class Blueprint:
    blueprints = []

    def process_input(content):
        blueprint_instructions = content.split("\n\n")
        blueprints = []
        for blueprint in blueprint_instructions:
            blueprint_stats = blueprint.split()
            blueprint_index = blueprint_stats[1][:-1]
            ore_robot_cost = (blueprint_stats[6], 0, 0)
            clay_robot_cost = (blueprint_stats[12], 0, 0)
            obsidian_robot_cost = (
                blueprint_stats[18],
                blueprint_stats[21],
                0,
            )
            geode_robot_cost = (
                blueprint_stats[27],
                0,
                blueprint_stats[30],
            )
            blueprints.append(
                Blueprint(
                    blueprint_index,
                    ore_robot_cost,
                    clay_robot_cost,
                    obsidian_robot_cost,
                    geode_robot_cost,
                )
            )
        Blueprint.blueprints = blueprints

    def __init__(
        self,
        blueprint_index,
        ore_robot_cost,
        clay_robot_cost,
        obsidian_robot_cost,
        geode_robot_cost,
    ) -> None:
        # Costs are defined as 3-element tuples, containing:
        #   - cost in ore
        #   - cost in clay
        #   - cost in obsidian
        # of each robot type.

        self.blueprint_index = blueprint_index
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost

    def __str__(self) -> str:
        result = (
            f"Blueprint {self.blueprint_index}:"
            + f"\n  Each ore robot costs {self.ore_robot_cost[0]} ore, {self.ore_robot_cost[1]} clay and {self.ore_robot_cost[2]} obsidian."
            + f"\n  Each clay robot costs {self.clay_robot_cost[0]} ore, {self.clay_robot_cost[1]} clay and {self.clay_robot_cost[2]} obsidian."
            + f"\n  Each obsidian robot {self.obsidian_robot_cost[0]} ore, {self.obsidian_robot_cost[1]} clay and {self.obsidian_robot_cost[2]} obsidian."
            + f"\n  Each geode robot costs {self.geode_robot_cost[0]} ore, {self.geode_robot_cost[1]} clay and {self.geode_robot_cost[2]} obsidian."
        )
        return result

    def get_robot_cost(self, robot_type):
        match robot_type:
            case "ore":
                cost = self.ore_robot_cost
            case "clay":
                cost = self.clay_robot_cost
            case "obsidian":
                cost = self.obsidian_robot_cost
            case "geode":
                cost = self.geode_robot_cost
        cost_dict = {"ore": cost[0], "clay": cost[1], "obsidian": cost[2]}
        return cost_dict


class Robot_Factory:
    def __init__(self, blueprint: Blueprint) -> None:
        self.current_resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
        self.current_robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        self.time_remaining = 24
        self.blueprint: Blueprint = blueprint

    def start_production(self):
        self.time_remaining = 24
        while self.time_remaining:
            self.time_remaining -= 1
            self.current_resources["ore"] += self.current_robots["ore"]
            self.current_resources["clay"] += self.current_robots["clay"]
            self.current_resources["obsidian"] += self.current_robots["obsidian"]
            self.current_resources["geode"] += self.current_robots["geode"]
            if (
                not self.insufficient_ore("geode")
                and self.calculate_best_move() == "geode"
            ):
                self.make_robot("geode")
            elif (
                not self.insufficient_ore("obsidian")
                and self.calculate_best_move() == "obsidian"
            ):
                self.make_robot("obsidian")
            elif (
                not self.insufficient_ore("clay")
                and self.calculate_best_move() == "clay"
            ):
                self.make_robot("clay")
            elif (
                not self.insufficient_ore("ore") and self.calculate_best_move() == "ore"
            ):
                self.make_robot("ore")

    def calculate_robot_cost(self, robot_type):
        resource_value = {"ore": 1, "clay": 1, "obsidian": 1}
        time_remaining = self.time_remaining - 1
        robot_cost = self.get_robot_cost(robot_type)
        if self.insufficient_ore(robot_type):
            for i in range(1, time_remaining + 1):
                if (
                    (
                        robot_cost["ore"]
                        - self.current_resources["ore"]
                        - i * self.current_robots["ore"]
                        <= 0
                    )
                    and (
                        robot_cost["clay"]
                        - self.current_resources["clay"]
                        - i * self.current_robots["clay"]
                        <= 0
                    )
                    and (
                        robot_cost["obsidian"]
                        - self.current_resources["obsidian"]
                        - i * self.current_robots["obsidian"]
                        <= 0
                    )
                ):
                    time_remaining -= 1
                    break
                if i == time_remaining:
                    time_remaining = 0

        robot_value = (
            time_remaining * resource_value[robot_type]
            - robot_cost["ore"] * resource_value["ore"]
            - robot_cost["clay"] * resource_value["clay"]
            - robot_cost["obsidian"] * resource_value["obsidian"]
        )
        return robot_value

    def calculate_best_move(self):
        ore_robot_value = self.calculate_robot_cost("ore")
        clay_robot_value = self.calculate_robot_cost("clay")
        obsidian_robot_value = self.calculate_robot_cost("obsidian")
        geode_robot_value = self.calculate_robot_cost("geode")
        robot_values = [
            ore_robot_value,
            clay_robot_value,
            obsidian_robot_value,
            geode_robot_value,
        ]
        if clay_robot_value == max(robot_values):
            return "clay"
        if obsidian_robot_value == max(robot_values):
            return "obsidian"
        if geode_robot_value == max(robot_values):
            return "geode"

    def make_robot(self, robot_type):
        self.spend_resources(robot_type)
        self.add_robot(robot_type)

    def add_robot(self, robot_type):
        match robot_type:
            case "ore":
                self.current_robots["ore"] += 1
            case "clay":
                self.current_robots["clay"] += 1
            case "obsidian":
                self.current_robots["obsidian"] += 1
            case "geode":
                self.current_robots["geode"] += 1

    def spend_resources(self, robot_type):
        if self.insufficient_ore(robot_type):
            raise Exception("Not enough resources!")
        cost = self.get_robot_cost(robot_type)
        self.current_resources["ore"] -= cost["ore"]
        self.current_resources["clay"] -= cost["clay"]
        self.current_resources["obsidian"] -= cost["obsidian"]

    def insufficient_ore(self, robot_type):
        cost = self.get_robot_cost(robot_type)
        return (
            cost["ore"] > self.current_resources["ore"]
            or cost["clay"] > self.current_resources["clay"]
            or cost["obsidian"] > self.current_resources["obsidian"]
        )

    def get_robot_cost(self, robot_type):
        return self.blueprint.get_robot_cost(robot_type)


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    Blueprint.process_input(content)
