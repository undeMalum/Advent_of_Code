import pytest
import pathlib
import day_6

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize("test_string, expected_result", [
    ("abcdqwre", True),
    ("fghjdsf", False),
    ("ffff", False),
    ("ffoo", False),
    ("deradom", False)
])
def test_is_marker(test_string, expected_result):
    assert day_6.is_marker(test_string) is expected_result


@pytest.fixture()
def puzzle_example():
    puzzle = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return puzzle


def test_find_marker_3(puzzle_example):
    """Test find_marker with a chunk of length 3"""
    assert day_6.find_marker(puzzle_example, 4) == 7


def test_find_marker_14(puzzle_example):
    """Test find_marker with a chunk of length 14"""
    assert day_6.find_marker(puzzle_example, 14) == 19
