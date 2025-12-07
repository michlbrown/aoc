import math


def part1(contents: list[str]):
    total = 0
    lines = [line.split() for line in contents]
    nums = [list(map(lambda n: int(n), line)) for line in lines[:-1]]
    operations = lines[-1]
    problem_amt = len(nums[0])

    for problem_num in range(0, problem_amt):
        operands = [nums[row][problem_num] for row in range(0, len(nums))]
        match operations[problem_num]:
            case "+":
                total += int(sum(operands))
            case "*":
                total += int(math.prod(operands))

    print(total)


with open("input.txt") as f:
    contents = [line for line in f]

part1(contents)
