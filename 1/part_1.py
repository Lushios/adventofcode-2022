with open("input.txt") as file:
    data = file.read().splitlines()

fattest_elf_alive = 0
current_elf_fatness = 0
for calorie_item in data:
    if calorie_item == '':
        if current_elf_fatness > fattest_elf_alive:
            fattest_elf_alive = current_elf_fatness
        current_elf_fatness = 0
    else:
        current_elf_fatness += int(calorie_item)

print(fattest_elf_alive)
