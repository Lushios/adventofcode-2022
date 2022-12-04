with open("input.txt") as file:
    data = file.read().splitlines()

counter = 0
for pair in data:
    first_str, second_str = pair.split(',')
    first, second = list(map(int, first_str.split('-'))), list(map(int, second_str.split('-')))
    first, second = range(first[0], first[1]), range(second[0], second[1])
    if (
        (second.start <= first.start <= second.stop)
        or (first.start <= second.start <= first.stop)
    ):
        counter += 1
print(counter)
