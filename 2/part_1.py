with open("input.txt") as file:
    data = file.read().splitlines()

transform = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

win_conditions = {
    "B": "A",
    "C": "B",
    "A": "C",
}

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

my_score = 0
for game in data:
    them, me = game.split(" ", 1)
    me = transform[me]
    my_score += scores[me]
    if me == them:
        my_score += 3
    elif win_conditions[me] == them:
        my_score += 6
print(my_score)
