import advent_of_code.puzzle_06 as p06
from nose.tools import assert_equal
import os

sample_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "06_input.txt")


def test_part_1_sample_input():
    largest = p06.part_1(sample_input)
    assert_equal(largest[0], 4, f"Expected largest patch to have id 4, but got {largest[0]}")
    assert_equal(largest[1], 17, f"Expected largest patch to be of size 17, but was {largest[1]}")


def test_part_1_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip().split("\n")
    largest = p06.part_1(real_input)
    assert_equal(largest[0], 33, f"Expected largest patch to have id 33, but got {largest[0]}")
    assert_equal(largest[1], 3933, f"Expected largest patch to be of size 3933, but was {largest[1]}")


def test_part_2_sample_input():
    region_size = p06.part_2(sample_input, 32)
    assert_equal(region_size, 16, f"Expected the region size to be 16, but was {region_size}")


def test_part_2_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip().split("\n")
    region_size = p06.part_2(real_input, 10000)
    assert_equal(region_size, 41145, f"Expected region size to be 41145, but was {region_size}")
