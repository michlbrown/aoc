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


def part2(contents: list[str]):
    # separate operands from operators
    operators = contents[-1].split()
    cols = contents[:-1]
    cols = list(zip(*cols))  # rotate to get a column at each index

    total = 0
    operands = []
    problem_num = 0
    for col in cols:
        if set(col) in ({" "}, {"\n"}):
            match operators[problem_num]:
                case "+":
                    total += sum(operands)
                case "*":
                    total += math.prod(operands)

            problem_num += 1
            operands = []
        else:
            print(col)
            operands.append(int("".join(col)))

    print(total)


with open("input.txt") as f:
    contents = [line for line in f]

part1(contents)
part2(contents)
