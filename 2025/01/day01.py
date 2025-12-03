import math

START = 50
DIAL_MIN = 0
DIAL_MAX = 100


def part_one(rotations: list[str]):
    password = 0
    current = START

    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])

        if direction == "L":
            amount *= -1

        change = current + amount
        current = change % DIAL_MAX
        if current == 0:
            password += 1

    return password


def part_two(rotations: list[str]):
    password = 0
    current = START

    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])
        full_rotations = math.floor(amount / 100)
        remainder = amount - full_rotations * 100
        password += full_rotations

        if direction == "L":
            new = (current - remainder) % 100
            if new == 0:
                password += 1
            elif current != 0 and new > current:
                password += 1
        else:
            new = (current + remainder) % 100
            if new < current:
                password += 1

        current = new
    return password


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

print(part_one(lines))
print(part_two(lines))
