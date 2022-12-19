class Monkey:
    monkeys = []
    operations = [
        lambda x: x * 5,
        lambda x: x + 3,
        lambda x: x + 7,
        lambda x: x + 5,
        lambda x: x + 2,
        lambda x: x * 19,
        lambda x: x**2,
        lambda x: x + 4,
    ]
    big_divisor = 1
    part_2_triggered = False

    def trigger_part_2():
        Monkey.monkeys = []
        Monkey.big_divisor = 1
        Monkey.part_2_triggered = True

    def __init__(self, monkey_stats) -> None:
        self.items = []
        self.set_items(monkey_stats)
        self.operation = None
        self.set_operation(monkey_stats)
        self.test = None
        self.set_test(monkey_stats)
        self.true_throw = -1
        self.set_true_throw(monkey_stats)
        self.false_throw = -1
        self.set_false_throw(monkey_stats)
        self.inspection_counter = 0

    def inspect(self, item):
        item = self.operation(item)
        if Monkey.part_2_triggered == True:
            item %= Monkey.big_divisor
        else:
            item //= 3
        self.inspection_counter += 1
        return item

    def test_and_throw(self, item):
        if self.test(item):
            self.throw(item, self.true_throw)
        else:
            self.throw(item, self.false_throw)

    def throw(self, item, receiver_monkey_index):
        receiver_monkey = Monkey.monkeys[receiver_monkey_index]
        receiver_monkey.items.append(item)

    def take_turn(self):
        for item in self.items:
            new_item = self.inspect(item)
            self.test_and_throw(new_item)
        self.items = []

    def set_items(self, monkey_stats):
        items = monkey_stats[1].split()[2:]
        for item in items:
            self.items.append(int(item.replace(",", "")))

    def set_operation(self, monkey_stats):
        monkey_index = int(monkey_stats[0].split()[1].replace(":", ""))
        self.operation = Monkey.operations[monkey_index]

    def set_test(self, monkey_stats):
        test_divisor = int(monkey_stats[3].split()[-1])
        Monkey.big_divisor *= test_divisor
        self.test = lambda x: x % test_divisor == 0

    def set_true_throw(self, monkey_stats):
        self.true_throw = int(monkey_stats[4].split()[-1])

    def set_false_throw(self, monkey_stats):
        self.false_throw = int(monkey_stats[5].split()[-1])

    def display_monkey_stats(self):
        print(
            f"""    Monkey:
        Starting items: {self.items}
        Operation: {self.operation}
        Test: {self.test}
            If true: throw to monkey {self.true_throw}
            If false: throw to monkey {self.false_throw}"""
        )


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()

    monkey_list = content.split("\n\n")
    for i in range(len(monkey_list)):
        monkey_stats = monkey_list[i].split("\n")
        Monkey.monkeys.append(Monkey(monkey_stats))

    for _ in range(20):
        for monkey in Monkey.monkeys:
            monkey.take_turn()

    inspection_counters = []

    for monkey in Monkey.monkeys:
        inspection_counters.append(monkey.inspection_counter)

    inspection_counters.sort(reverse=True)
    print(inspection_counters[0] * inspection_counters[1])

    Monkey.trigger_part_2()
    for i in range(len(monkey_list)):
        monkey_stats = monkey_list[i].split("\n")
        Monkey.monkeys.append(Monkey(monkey_stats))

    for i in range(10000):
        for monkey in Monkey.monkeys:
            monkey.take_turn()

    inspection_counters = []

    for monkey in Monkey.monkeys:
        inspection_counters.append(monkey.inspection_counter)

    inspection_counters.sort(reverse=True)
    print(inspection_counters[0] * inspection_counters[1])
