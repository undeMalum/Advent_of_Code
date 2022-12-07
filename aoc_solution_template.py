import pathlib
import sys


def parse(puzzle_input_f):
    """Parse input."""


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
