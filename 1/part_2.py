with open("input.txt") as file:
    data = file.read().splitlines()

three_fattest_elves_alive = []
current_elf_fatness = 0
for calorie_item in data:
    if calorie_item == '':
        three_fattest_elves_alive.append(current_elf_fatness)
        #  feels like using max() would be both simpler and quicker
        if len(three_fattest_elves_alive) > 3:
            three_fattest_elves_alive.remove(min(three_fattest_elves_alive))
        current_elf_fatness = 0
    else:
        current_elf_fatness += int(calorie_item)

print(sum(three_fattest_elves_alive))
