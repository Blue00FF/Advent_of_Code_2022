from main import *

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def test_inspection_counter_part_1():
    Monkey.operations = [
        lambda x: x * 19,
        lambda x: x + 6,
        lambda x: x**2,
        lambda x: x + 3,
    ]

    monkey_list = test_input.split("\n\n")
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
    assert inspection_counters[0] * inspection_counters[1] == 10605


def test_inspection_counter_part_2():
    Monkey.trigger_part_2()

    monkey_list = test_input.split("\n\n")
    for i in range(len(monkey_list)):
        monkey_stats = monkey_list[i].split("\n")
        Monkey.monkeys.append(Monkey(monkey_stats))

    for _ in range(10000):
        for monkey in Monkey.monkeys:
            monkey.take_turn()

    inspection_counters = []

    for monkey in Monkey.monkeys:
        inspection_counters.append(monkey.inspection_counter)

    inspection_counters.sort(reverse=True)
    assert inspection_counters[0] * inspection_counters[1] == 2713310158
