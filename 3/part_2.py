from functools import reduce

def get_char_value(char: str):
    value = ord(char)
    if char.isupper():
        value -= 38
    else:
        value -= 96
    return value


with open("input.txt") as file:
    data = file.read().splitlines()

final_score = 0
group = []
for line in data:
    group.append(set(line))
    if len(group) < 3:
        continue
    badge = reduce(lambda x, y: x & y, group).pop()
    final_score += get_char_value(badge)
    group = []
print(final_score)

