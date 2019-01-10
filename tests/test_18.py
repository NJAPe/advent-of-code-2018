import advent_of_code.puzzle_18 as p18
from nose.tools import assert_equal, assert_true, assert_false
import os

input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "18_input.txt")

sample_input = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

sample_in_parsed = [[".", "#", ".", "#", ".", ".", ".", "|", "#", "."],
                    [".", ".", ".", ".", ".", "#", "|", "#", "#", "|"],
                    [".", "|", ".", ".", "|", ".", ".", ".", "#", "."],
                    [".", ".", "|", "#", ".", ".", ".", ".", ".", "#"],
                    ["#", ".", "#", "|", "|", "|", "#", "|", "#", "|"],
                    [".", ".", ".", "#", ".", "|", "|", ".", ".", "."],
                    [".", "|", ".", ".", ".", ".", "|", ".", ".", "."],
                    ["|", "|", ".", ".", ".", "#", "|", ".", "#", "|"],
                    ["|", ".", "|", "|", "|", "|", ".", ".", "|", "."],
                    [".", ".", ".", "#", ".", "|", ".", ".", "|", "."]]
sample_after_one_min = [[".", ".", ".", ".", ".", ".", ".", "#", "#", "."],
                        [".", ".", ".", ".", ".", ".", "|", "#", "#", "#"],
                        [".", "|", ".", ".", "|", ".", ".", ".", "#", "."],
                        [".", ".", "|", "#", "|", "|", ".", ".", ".", "#"],
                        [".", ".", "#", "#", "|", "|", ".", "|", "#", "|"],
                        [".", ".", ".", "#", "|", "|", "|", "|", ".", "."],
                        ["|", "|", ".", ".", ".", "|", "|", "|", ".", "."],
                        ["|", "|", "|", "|", "|", ".", "|", "|", ".", "|"],
                        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
                        [".", ".", ".", ".", "|", "|", ".", ".", "|", "."]]


def test_parse_input_sample_input():
    parsed = p18.parse_input(sample_input)
    for y in range(len(sample_in_parsed)):
        assert_equal(parsed[y], sample_in_parsed[y], f"wrong area parsed on line y={y}")


def test_step_one_minute_sample_input():
    parsed = p18.parse_input(sample_input)
    parsed = p18.step_one_minute(parsed)
    for y in range(len(sample_after_one_min)):
        assert_equal(parsed[y], sample_after_one_min[y], f"wrong area parsed on line y={y}")


def test_count_after_10_min_sample_input():
    num_lumberyards, num_open, num_trees = p18.count_after_10_min(sample_input)
    print(str(num_open)+" "+str(num_trees)+" "+str(num_lumberyards))
    assert_equal(num_open, 32, "Wrong number of open acres")
    assert_equal(num_trees, 37, "Wrong number of wooded acres")
    assert_equal(num_lumberyards, 31, "Wrong number of lumberyards")


def test_part_1_sample_input():
    answer = p18.part_1(sample_input)
    assert_equal(answer, 1147)


def test_part_1_real():
    with open(input_file_path) as f:
        raw_input = f.read().strip()
    answer = p18.part_1(raw_input)
    assert_equal(answer, 466312)


def test_part_2_real():
    with open(input_file_path) as f:
        raw_input = f.read().strip()
    answer = p18.part_2(raw_input)
    assert_equal(answer, 176782)
