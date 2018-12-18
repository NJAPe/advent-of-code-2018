import advent_of_code.puzzle_03 as p03
from nose.tools import assert_equal
import os

sample_input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2", ""]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "03_input.txt")


def test_part_1_sample_input():
    number_of_patches = len(p03.get_intersection_patches(sample_input))
    assert_equal(number_of_patches, 4, f"expected 4 overlapping patches, but got {number_of_patches}")


def test_part_1_real_input():
    my_input = p03.get_input_from_file(input_file_path)
    number_of_patches = len(p03.get_intersection_patches(my_input))
    assert_equal(number_of_patches, 121163, f"expected 4 overlapping patches, but got {number_of_patches}")


def test_part_2_sample_input():
    non_overlapping_id = p03.get_non_intersecting_patch(sample_input)
    assert_equal(non_overlapping_id, 3, f"expected id 3 but got {non_overlapping_id}")


def test_part_2_real_input():
    my_input = p03.get_input_from_file(input_file_path)
    non_overlapping_id = p03.get_non_intersecting_patch(my_input)
    assert_equal(non_overlapping_id, 943, f"expected id 3 but got {non_overlapping_id}")
