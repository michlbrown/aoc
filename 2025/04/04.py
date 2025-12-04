def is_accessible(grid: list[str], row: int, col: int):
    MAX_ADJACENT = 4
    num_adjacent = 0

    for i in range(max(0, row - 1), min(row + 2, len(grid))):
        for j in range(max(0, col - 1), min(col + 2, len(grid[i]))):
            if (i, j) != (row, col) and grid[i][j] == "@":
                num_adjacent += 1

    return num_adjacent < MAX_ADJACENT


def part1(grid: list[str]):
    accessible_rolls = 0

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == "@":
                if is_accessible(grid, i, j):
                    accessible_rolls += 1
    return accessible_rolls


with open("input.txt") as f:
    contents = [line.rstrip() for line in f.readlines()]

print(part1(contents))
