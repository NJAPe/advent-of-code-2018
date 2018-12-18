import advent_of_code.puzzle_05 as p05
from nose.tools import assert_equal
import os

sample_input = "dabAcCaCBAcCcaDA"
sample_input_collapse_end = "aAbBcCddD"
sample_input_no_collapse = "aabAAB"
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "05_input.txt")


def test_part_1_sample_input():
    collapsed = p05.collapse_polymer(sample_input)
    assert_equal(len(collapsed), 10, f"expected 10 characters to remain, but {len(collapsed)} remained")


def test_part_1_collapse_ends():
    collapsed = p05.collapse_polymer(sample_input_collapse_end)
    assert_equal(len(collapsed), 1, f"expected 1 character to remain, but {len(collapsed)} remained")


def test_part_1_no_collapse():
    collapsed = p05.collapse_polymer(sample_input_no_collapse)
    assert_equal(collapsed, sample_input_no_collapse, "Polymer should not have changed")


def test_part_1_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip()
    collapsed = p05.collapse_polymer(real_input)
    assert_equal(len(collapsed), 11720, f"expected 11720 characters to remain, but {len(collapsed)} remained")


def test_part_2_sample_input():
    shortest = p05.find_shortest_poly_by_removing_one_type(sample_input)
    assert_equal(len(shortest), 4, f"expected 4 characters to remain, but {len(shortest)} remained")


def test_part_2_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip()
    shortest = p05.find_shortest_poly_by_removing_one_type(real_input)
    assert_equal(len(shortest), 4956, f"exected 4956 characters to remain, but {len(shortest)} remained")
