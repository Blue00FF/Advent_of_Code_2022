class Elf_Device:
    CYCLES_TO_APPRAISE = [20, 60, 100, 140, 180, 220]

    def __init__(self) -> None:
        self.cycles = []
        self.total_signal_strength = 0

    def run_CPU(self, instructions):
        split_input = instructions.split("\n")
        register = 1
        self.cycles = []
        for line in split_input:
            if line[:4] == "noop":
                self.cycles.append(register)
            if line[:4] == "addx":
                self.cycles.append(register)
                register += int(line.split()[1])
                self.cycles.append(register)

    def appraise_signal_strength(self):
        self.total_signal_strength = 0
        for index in self.CYCLES_TO_APPRAISE:
            self.total_signal_strength += self.cycles[index - 2] * index


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read()
    device = Elf_Device()
    device.run_CPU(instructions)
    device.appraise_signal_strength()
    print(device.total_signal_strength)
