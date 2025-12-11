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


# I don't think this is a general solution
# Uses assumptions and shape of input data
def part2(points: list[Point]):
    rects = [Rect(a, b) for a, b in combinations(points, 2)]
    rects.sort(key=lambda r: r.area(), reverse=True)

    edges = [(a, b) for a, b in zip(points, points[1:])]
    edges.append((points[-1], points[0]))

    for rect in rects:
        rx1 = min(rect.a.x, rect.b.x)
        rx2 = max(rect.a.x, rect.b.x)
        ry1 = min(rect.a.y, rect.b.y)
        ry2 = max(rect.a.y, rect.b.y)

        # reject if a edge intersects through rectangle
        intersects = False
        for p1, p2 in edges:
            ex1 = min(p1.x, p2.x)
            ex2 = max(p1.x, p2.x)
            ey1 = min(p1.y, p2.y)
            ey2 = max(p1.y, p2.y)

            if ex2 > rx1 and ex1 < rx2 and ey1 > ry1 and ey2 < ry2:
                intersects = True
                break

        if not intersects:
            print(rect.area())
            return


with open("input.txt") as f:
    points = [line.rstrip().split(",") for line in f]
    points = [Point(*map(int, point)) for point in points]

part1(points)
part2(points)
