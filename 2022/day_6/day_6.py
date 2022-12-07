from aocd.models import Puzzle
from aocd import submit


def is_marker(chunks_of_input: str) -> bool:
    for char in chunks_of_input:
        if char in chunks_of_input.replace(char, "", 1):
            return False
    return True


def find_marker(puzzle_input: str, chunk_length: int) -> int:
    start = 0
    end = chunk_length
    for char in range(len(puzzle_input)):
        if is_marker(puzzle_input[start:end]):
            return end
        start += 1
        end += 1


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=6)
    nth_char = find_marker(puzzle.input_data, 4)
    nth_char_msg = find_marker(puzzle.input_data, 14)
    to_submit = input("Do you want to submit your answer(y/n): ").lower()
    if to_submit == "y":
        submit(nth_char, part="a", year=2022, day=6)
        submit(nth_char_msg, part="b", year=2022, day=6)
    else:
        print(f"Answer part a: {nth_char}\nAnswer part b: {nth_char_msg}")
