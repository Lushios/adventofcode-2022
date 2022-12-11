LEAST_COMMON_MULTIPLE = 9699690


class Monkey:
    def __init__(self, text_monkey):
        monkey_parameters = text_monkey.split("\n")
        items = monkey_parameters[1].split(": ")[1]
        self.items = list(map(int, items.split(", ")))

        operation = monkey_parameters[2].split("old ")[1]
        operation_parameters = operation.split(" ")
        if operation_parameters[1] == "old":
            self.operation = lambda x: x * x
        elif operation_parameters[0] == "+":
            self.operation = lambda x: x + int(operation_parameters[1])
        else:
            self.operation = lambda x: x * int(operation_parameters[1])

        divisible_by = int(monkey_parameters[3].split(" ")[-1])
        if_test_true = int(monkey_parameters[4][-1])
        if_test_false = int(monkey_parameters[5][-1])
        self.get_throw_target = lambda x: if_test_true if x % divisible_by == 0 else if_test_false
        self.items_inspected = 0

    @property
    def hands_are_not_empty(self):
        return bool(self.items)

    def inspect_item(self):
        self.items[0] = self.operation(self.items[0])
        self.items[0] = self.items[0] % LEAST_COMMON_MULTIPLE
        self.items_inspected += 1

    def throw_item(self):
        target = self.get_throw_target(self.items[0])
        return target, self.items.pop(0)

    def catch_item(self, item):
        self.items.append(item)


class MonkeysPack:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def run_game(self, rounds_count):
        for i in range(0, rounds_count):
            self.run_round()
        return [monkey.items_inspected for monkey in self.monkeys]

    def run_round(self):
        for monkey in monkeys:
            self.run_turn(monkey)

    def run_turn(self, monkey):
        while monkey.hands_are_not_empty is True:
            monkey.inspect_item()
            target, item = monkey.throw_item()
            print(monkey.items)
            self.monkeys[target].catch_item(item)


with open("input.txt") as file:
    data = file.read()

monkeys = []
monkey_blocks = data.split("\n\n")
for monkey_block in monkey_blocks:
    monkeys.append(Monkey(monkey_block))

monkeys_pack = MonkeysPack(monkeys)

monkey_points = monkeys_pack.run_game(10000)
monkey_points = sorted(monkey_points)
print(monkey_points[-1] * monkey_points[-2])
