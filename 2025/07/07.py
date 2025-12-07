def part2(contents: list[str]):
    beams = list(map(lambda i: 1 if i == "S" else 0, contents[0]))
    for row in contents[2:]:
        for i, val in enumerate(row):
            if val == "^" and beams[i]:
                beams[i - 1] += beams[i]
                beams[i + 1] += beams[i]
                beams[i] = 0

    print(sum(beams))


def part1(contents: list[str]):
    splits = 0
    beams = list(map(lambda i: True if i == "S" else False, contents[0]))

    for row in contents[1:]:
        for i, val in enumerate(row):
            if val == "^" and beams[i]:
                splits += 1
                beams[i - 1] = True
                beams[i] = False
                beams[i + 1] = True

    print(splits)


with open("input.txt") as f:
    contents = [line.rstrip() for line in f]

part1(contents)
part2(contents)
