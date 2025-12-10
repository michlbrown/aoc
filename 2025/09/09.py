from dataclasses import dataclass
from itertools import combinations


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Rect:
    a: Point
    b: Point

    def area(self) -> int:
        width = abs(self.a.x - self.b.x) + 1
        height = abs(self.a.y - self.b.y) + 1
        return width * height


def part1(points: list[Point]):
    rects = [Rect(a, b) for a, b in combinations(points, 2)]
    rects.sort(key=lambda r: r.area(), reverse=True)
    print(rects[0].area())


with open("example.txt") as f:
    points = [line.rstrip().split(",") for line in f]
    points = [Point(*map(int, point)) for point in points]

part1(points)
