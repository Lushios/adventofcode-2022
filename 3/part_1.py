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

for line in data:
    middle_point = int(len(line)/2)
    first, second = (line[0:middle_point], line[middle_point:])
    duplicates = set(first) & set(second)
    final_score += sum(get_char_value(character) for character in duplicates)

print(final_score)
