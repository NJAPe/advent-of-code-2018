import advent_of_code.puzzle_13 as p13
from nose.tools import assert_equal
import os

sample_input = r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/"""
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "13_input.txt")


def remove_carts(line):
    tmp_line = line.replace(">", "-")
    tmp_line = tmp_line.replace(">", "-")
    tmp_line = tmp_line.replace("^", "|")
    tmp_line = tmp_line.replace("v", "|")
    return tmp_line


def test_parse_input_sample():
    carts, tunnel_system = p13.parse_input(sample_input)
    assert_equal(len(carts), 2, "wrong number of carts")
    assert_equal(carts[0].get_coordinates(), (2, 0), "Wrong cart 0 coordinates")
    assert_equal(carts[1].get_coordinates(), (9, 3), "Wrong cart 1 coordinates")
    stripped_system = sample_input.strip()
    for idx, line in enumerate(stripped_system.split("\n")):
        assert_equal(tunnel_system[idx], remove_carts(line), f"wrong tunnel system on y-pos {idx}")


def test_find_first_crash_sample():
    crash_coord = p13.find_first_crash(sample_input)
    assert_equal(crash_coord, (7, 3), "Wrong coordinates in first crash")


def test_find_first_crash_real():
    with open(input_file_path) as f:
        my_input = f.read()
    crash_coord = p13.find_first_crash(my_input)
    assert_equal(crash_coord, (118, 66), "Wrong coordinates in first crash")
