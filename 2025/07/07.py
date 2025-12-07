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
