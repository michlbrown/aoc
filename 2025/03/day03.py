def part1(banks: list[str]):
    total = 0
    for bank in banks:
        bank = list(bank)
        # get the index and value of the max possible first digit
        first_idx, first_digit = max(enumerate(bank[:-1]), key=lambda x: x[1])
        second_digit = max(bank[first_idx + 1 :])
        total += int(first_digit + second_digit)

    return total


with open("input.txt") as f:
    contents = [line.rstrip() for line in f.readlines()]

print(part1(contents))
