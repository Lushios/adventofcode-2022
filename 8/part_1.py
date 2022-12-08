from numpy import array

with open("input.txt") as file:
    data = file.read().splitlines()

data = [list(map(int, list(line))) for line in data]

trees = array(data)

visible_trees = 99*99
for line_number, line in enumerate(trees):
    for column_number, tree in enumerate(line):
        if 0 in (line_number, column_number) or 98 in (line_number, column_number):
            continue
        if (
                max(trees[:line_number, column_number]) >= tree
                and max(trees[line_number + 1:, column_number]) >= tree
                and max(trees[line_number, :column_number]) >= tree
                and max(trees[line_number, column_number + 1:]) >= tree
        ):
            visible_trees -= 1

print(visible_trees)

