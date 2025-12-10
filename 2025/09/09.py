from itertools import combinations


def part1(points):
    areas = []
    for (x1, y1), (x2, y2) in combinations(points, 2):
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        areas.append(width * height)

    print(sorted(areas, reverse=True)[0])


with open("input.txt") as f:
    points = [line.rstrip().split(",") for line in f]
    points = [tuple(map(int, point)) for point in points]

part1(points)
