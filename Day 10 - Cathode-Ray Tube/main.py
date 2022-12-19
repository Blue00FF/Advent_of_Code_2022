class Elf_Device:
    CYCLES_TO_APPRAISE = [20, 60, 100, 140, 180, 220]
    END_OF_SCREEN_LINE = [0, 40, 80, 120, 160, 200, 240]

    def __init__(self) -> None:
        self.register_history = []
        self.cumulative_signal_strength = 0
        self.image = []

    def run_CPU(self, instructions):
        split_input = instructions.split("\n")
        register = 1
        self.register_history = []
        for line in split_input:
            if line[:4] == "noop":
                self.register_history.append(register)
            if line[:4] == "addx":
                self.register_history.append(register)
                self.register_history.append(register)
                register += int(line.split()[1])

    def appraise_signal_strength(self):
        self.cumulative_signal_strength = 0
        for index in self.CYCLES_TO_APPRAISE:
            self.cumulative_signal_strength += self.register_history[index - 1] * index

    def generate_screen_image(self):
        self.image = ""
        for index, register in enumerate(self.register_history):
            if index % 40 in [register - 1, register, register + 1]:
                self.image += "#"
            else:
                self.image += "."

    def display_screen(self):
        for index in range(1, len(self.END_OF_SCREEN_LINE)):
            print(
                self.image[
                    self.END_OF_SCREEN_LINE[index - 1] : self.END_OF_SCREEN_LINE[index]
                ]
            )


if __name__ == "__main__":
    with open("input.txt") as f:
        instructions = f.read()
    device = Elf_Device()
    device.run_CPU(instructions)
    device.appraise_signal_strength()
    # print(device.cumulative_signal_strength)
    device.generate_screen_image()
    device.display_screen()
