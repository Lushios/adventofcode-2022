with open("input.txt") as file:
    data = file.read().splitlines()

win_conditions = {
    "A": "B",
    "B": "C",
    "C": "A",
}

lose_conditions = {value: key for key, value in win_conditions.items()}

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

my_score = 0
for game in data:
    them, result = game.split(" ", 1)
    if result == "Y":
        my_score += 3
        me = them
    elif result == "Z":
        my_score += 6
        me = win_conditions[them]
    else:
        me = lose_conditions[them]
    my_score += scores[me]

print(my_score)
