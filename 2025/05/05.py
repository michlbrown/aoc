def merge_ranges(ranges: list[tuple[int, int]]):
    merged = []
    ranges.sort(key=lambda x: x[0])

    merged = [ranges[0]]
    for current in ranges[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current

        if curr_start <= prev_end:
            merged[-1] = (prev_start, max(curr_end, prev_end))
        else:
            merged.append(current)

    return merged


def part1(fresh_ranges: list[tuple[int, int]], ingredients: list[int]):
    fresh_ranges = merge_ranges(fresh_ranges)  # sorted in increasing order
    num_fresh = 0
    for id in ingredients:
        for range in fresh_ranges:
            start, end = range
            if id < start:
                break
            elif id > end:
                continue
            elif start <= id <= end:
                num_fresh += 1
                break

    return num_fresh


first: list[str] = []
second: list[str] = []

with open("input.txt") as f:
    target = first
    for line in f:
        if line.strip() == "":
            target = second
            continue

        target.append(line.rstrip())

fresh_ranges: list[tuple[int, int]] = []
for line in first:
    line = line.split("-")
    fresh_ranges.append((int(line[0]), int(line[1])))

ingredients = [int(line) for line in second]

print(part1(fresh_ranges, ingredients))
