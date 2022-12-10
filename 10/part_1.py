class Instruction:
    def __init__(self, instruction_type, value=0):
        self.instruction_type = instruction_type
        self.value = value
        if instruction_type == 'noop':
            self.ticks_to_live = 1
        elif instruction_type == 'addx':
            self.ticks_to_live = 2

    def tick(self):
        self.ticks_to_live -= 1

    @property
    def is_finished(self):
        return self.ticks_to_live == 0


class Game:
    def __init__(self):
        self.cycle_counter = 0
        self.current_instruction = None
        self.x = 1
        self.important_results = []

    def run_instruction(self, instruction: str):
        instruction = instruction.split(' ')
        if instruction[0] == 'noop':
            instruction = Instruction('noop')
        elif instruction[0] == 'addx':
            instruction = Instruction('addx', int(instruction[1]))
        self.current_instruction = instruction
        instruction_over = False
        while instruction_over is False:
            instruction_over = self.tick()

    def tick(self):
        self.cycle_counter += 1
        if self.important_cycle():
            self.important_results.append(self.x * self.cycle_counter)
        self.current_instruction.tick()
        if self.current_instruction.is_finished:
            self.x += self.current_instruction.value
        # if self.important_cycle():
        #     self.important_results.append(self.x * self.cycle_counter)
        return self.current_instruction.is_finished

    def important_cycle(self):
        return self.cycle_counter == 20 or ((self.cycle_counter - 20) % 40 == 0 and self.cycle_counter <= 220)


with open("input.txt") as file:
    data = file.read().splitlines()

game = Game()
for line in data:
    game.run_instruction(line)

print(sum(game.important_results))
