from collections import Counter, namedtuple
from itertools import combinations
from math import dist

NUM_CONNECTIONS = 1000
Point = namedtuple("Point", ["x", "y", "z"])
PairDist = namedtuple("PairDist", ["p1_idx", "p2_idx", "dist"])


# Disjoint Set Union
class DSU:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # already part of the same union

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def part1(points: list[Point]):
    n = len(points)
    pair_dists = []
    for (i, p1), (j, p2) in combinations(enumerate(points), 2):
        d = dist(p1, p2)
        pair_dists.append(PairDist(i, j, d))

    pair_dists.sort(key=lambda p: p.dist)
    dsu = DSU(n)

    used = 0
    for i, j, _ in pair_dists:
        dsu.union(i, j)
        used += 1
        if used == NUM_CONNECTIONS:
            break

    counts = Counter(dsu.find(i) for i in range(n))
    sizes = sorted(counts.values(), reverse=True)

    print(sizes[0] * sizes[1] * sizes[2])


with open("input.txt") as f:
    contents = [Point(*map(int, line.rstrip().split(","))) for line in f]

part1(contents)
