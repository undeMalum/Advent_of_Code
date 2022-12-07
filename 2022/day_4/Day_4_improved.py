import pathlib
import sys


def divide_string(init_string: str) -> [str, str]:
    temp = init_string.split(",")
    left_ids, right_ids = [numb.split("-") for numb in temp]
    return left_ids, right_ids


def parse(puzzle_input_f):
    """Parse input."""
    return [divide_string(pair) for pair in puzzle_input_f.split("/n")]


def part1(data_f):
    """Solve part 1."""


def part2(data_f):
    """Solve part 2."""


def solve(puzzle_input_f):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input_f)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
