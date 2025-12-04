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


def part2(ranges: list[tuple[int, int]]):
    invalid_ids = []

    for id_range in ranges:
        for id in range(id_range[0], id_range[1] + 1):
            id = str(id)

            for seq_len in range(1, len(id) // 2 + 1):
                # Check if ID can be equally split
                if len(id) % seq_len:
                    continue

                # Split ID into slices of size seq_len
                slices = [id[i : i + seq_len] for i in range(0, len(id), seq_len)]
                # Check if all slices are equal (repeated)
                invalid = len(set(slices)) == 1
                if invalid:
                    invalid_ids.append(int(id))
                    break

    return sum(invalid_ids)


with open("input.txt") as f:
    contents = f.readline().rstrip().split(",")

ranges = []
for s in contents:
    start, stop = s.split("-")
    ranges.append((int(start), int(stop)))

print(part1(ranges))
print(part2(ranges))
