LINE_SIZE = 40


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
        self.pixels_drawn = []
        self.lines = []

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
        current_pixel_drawn = (self.cycle_counter - 1) % LINE_SIZE
        if current_pixel_drawn in (self.x - 1, self.x, self.x + 1):
            self.pixels_drawn.append(current_pixel_drawn)
        if self.important_cycle():
            self.lines.append(self.pixels_drawn)
            self.pixels_drawn = []
        self.current_instruction.tick()
        if self.current_instruction.is_finished:
            self.x += self.current_instruction.value
        return self.current_instruction.is_finished

    def important_cycle(self):
        return self.cycle_counter % LINE_SIZE == 0 and self.cycle_counter <= 240


with open("input.txt") as file:
    data = file.read().splitlines()

game = Game()
for line in data:
    game.run_instruction(line)

for line in game.lines:
    string = [' '] * 40
    for character in line:
        string[character] = '█'
    print(''.join(string))
