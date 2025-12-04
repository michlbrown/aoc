def part1(ranges: list[tuple[int, int]]):
    invalid_ids = []
    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            id = str(id)
            middle = len(id) // 2
            left = id[:middle]
            right = id[middle:]
            if left == right:
                invalid_ids.append(int(id))

    return sum(invalid_ids)


with open("input.txt") as f:
    contents = f.readline().rstrip().split(",")

ranges = []
for s in contents:
    start, stop = s.split("-")
    ranges.append((int(start), int(stop)))

print(part1(ranges))
