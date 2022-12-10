with open("input.txt") as file:
    data = file.read().splitlines()


def U(a):
    a[1] += 1
    return a


def D(a):
    a[1] -= 1
    return a


def R(a):
    a[0] += 1
    return a


def L(a):
    a[0] -= 1
    return a


def move_tail(head, tail):
    if head[0] == tail[0] and abs(head[1] - tail[1]) >= 2:
        tail[1] += (head[1] - tail[1])//2
    elif head[1] == tail[1] and abs(head[0] - tail[0]) >= 2:
        tail[0] += (head[0] - tail[0])//2
    elif head[1] != tail[1] and head[0] != tail[0]:
        if abs(head[0] - tail[0]) >= 2:
            tail[0] += (head[0] - tail[0])//2
            tail[1] += head[1] - tail[1]
        elif abs(head[1] - tail[1]) >= 2:
            tail[1] += (head[1] - tail[1]) // 2
            tail[0] += head[0] - tail[0]

    return tail


head_location = [0, 0]
tail_location = [0, 0]
# simulate all points instead of just two, they all move relative to each other according to previous rules
# Maybe I can just count the first one, later ones take places of ones that came before them


unique_tail_locations = set()
for line in data:
    direction, number = line.split(' ')
    for _ in range(int(number)):
        head_location = locals()[direction](head_location)
        tail_location = move_tail(head_location, tail_location)
        unique_tail_locations.add(tuple(tail_location))

print(len(unique_tail_locations))
