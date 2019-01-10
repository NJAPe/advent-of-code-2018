import advent_of_code.puzzle_17 as p17
from nose.tools import assert_equal, assert_true, assert_false
import os
import sys


sample_input = """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
y=11, x=501..502"""
sample_topo = [[".", ".", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
               [".", "#", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", "."],
               [".", "#", ".", ".", "#", ".", ".", "#", ".", ".", ".", ".", ".", "."],
               [".", "#", ".", ".", "#", ".", ".", "#", ".", ".", ".", ".", ".", "."],
               [".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
               [".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
               [".", "#", "#", "#", "#", "#", "#", "#", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", "."],
               [".", ".", ".", ".", "#", ".", ".", "#", "#", ".", "#", ".", ".", "."],
               [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", "."],
               [".", ".", ".", ".", "#", "#", "#", "#", "#", "#", "#", ".", ".", "."]]
sample_topo_complete = [[".", ".", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", "|", ".", ".", ".", ".", ".", "#", "."],
               [".", "#", ".", ".", "#", "|", "|", "|", "|", ".", ".", ".", "#", "."],
               [".", "#", ".", ".", "#", "~", "~", "#", "|", ".", ".", ".", ".", "."],
               [".", "#", ".", ".", "#", "~", "~", "#", "|", ".", ".", ".", ".", "."],
               [".", "#", "~", "~", "~", "~", "~", "#", "|", ".", ".", ".", ".", "."],
               [".", "#", "~", "~", "~", "~", "~", "#", "|", ".", ".", ".", ".", "."],
               [".", "#", "#", "#", "#", "#", "#", "#", "|", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", ".", "."],
               [".", ".", ".", "|", "|", "|", "|", "|", "|", "|", "|", "|", ".", "."],
               [".", ".", ".", "|", "#", "~", "~", "~", "~", "~", "#", "|", ".", "."],
               [".", ".", ".", "|", "#", "~", "~", "#", "#", "~", "#", "|", ".", "."],
               [".", ".", ".", "|", "#", "~", "~", "~", "~", "~", "#", "|", ".", "."],
               [".", ".", ".", "|", "#", "#", "#", "#", "#", "#", "#", "|", ".", "."]]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "17_input.txt")


def test_parse_input_sample_topo():
    x_offset, min_y, max_y, topo = p17.parse_input(sample_input)
    assert_equal(x_offset, 494, "Wrong offset")
    assert_equal(min_y, 1, "Wrong min_y")
    assert_equal(max_y, 13, "wrong max_y")
    for y in range(len(sample_topo)):
        assert_equal(topo[y], sample_topo[y], f"Wrong topografy on y={y}")


def test_fill_water_sample_topo():
    x_offset, min_y, max_y, topo = p17.parse_input(sample_input)
    p17.fill_water(500 - x_offset, 0, p17.DOWN, "|", topo)
    for y in range(len(sample_topo_complete)):
        assert_equal(topo[y], sample_topo_complete[y], f"Wrong topografy on y={y}")


def test_part_1_sample_topo():
    still, flowing = p17.analyze_well(sample_input)
    assert_equal(still + flowing, 55)


def test_part_1_real():
    sys.setrecursionlimit(15000)
    with open(input_file_path) as f:
        raw_input = f.read().strip()
    still, flowing = p17.analyze_well(raw_input)
    assert_equal(still + flowing, 31412, "Wrong number of water")
    assert_equal(still, 25857, "Wrong number of still water")
    assert_equal(flowing, 5555, "Wrong number of flowing water")
