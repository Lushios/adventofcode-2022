from collections import defaultdict

with open("input.txt") as file:
    data = file.read().splitlines()

crates = defaultdict(list)
fuck_you_every_other_name_was_too_long_fuck_this_one_is_too_fuck = False
for line in data:
    if line == '':
        continue
    if fuck_you_every_other_name_was_too_long_fuck_this_one_is_too_fuck is False:
        for key, value in enumerate(range(1, len(line), 4)):
            if line[value] == '1':
                fuck_you_every_other_name_was_too_long_fuck_this_one_is_too_fuck = True
                break
            if line[value] != ' ':
                crates[key+1].insert(0, line[value])
    else:
        three_important_numbers = line.replace('move ', '').replace(' from', '').replace(' to', '')
        number, source, destination = list(map(int, three_important_numbers.split(' ')))
        for i in range(number):
            element = crates[source].pop()
            crates[destination].append(element)
response = ''
for i in range(1, len(crates) + 1):
    response += crates[i][-1]

print(response)
