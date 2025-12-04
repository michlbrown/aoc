def part1(banks: list[str]):
    total = 0
    for bank in banks:
        bank = list(bank)
        # get the index and value of the max possible first digit
        first_idx, first_digit = max(enumerate(bank[:-1]), key=lambda x: x[1])
        second_digit = max(bank[first_idx + 1 :])
        total += int(first_digit + second_digit)

    return total


def part2(banks: list[str]):
    total = 0
    for bank in banks:
        bank = list(bank)
        NUM_BATTERIES = 12

        # Initially the last 12 digits
        maximized = bank[-NUM_BATTERIES:]
        remaining = bank[:-NUM_BATTERIES]

        # work backwards through battery bank
        for b in reversed(remaining):
            # if adding b would increase value
            if b >= maximized[0]:
                # find inflection point
                i = 0
                while i + 1 < NUM_BATTERIES and maximized[i] >= maximized[i + 1]:
                    i += 1

                maximized.pop(i)
                maximized.insert(0, b)

        total += int("".join(maximized))
    return total


with open("input.txt") as f:
    contents = [line.rstrip() for line in f.readlines()]

print(part1(contents))
print(part2(contents))
