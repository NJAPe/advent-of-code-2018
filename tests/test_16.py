import advent_of_code.puzzle_16 as p16
from nose.tools import assert_equal, assert_true, assert_false
import os

input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "16_input.txt")

sample_input_1 = """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]

Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""


def test_parse_sample_input_sample_input_1():
    sample_1, line_idx = p16.parse_sample_inputs(sample_input_1)
    assert_equal(len(sample_1), 2, "Should be 2 inputs")
    assert_equal(sample_1[0][0], [3, 2, 1, 1], "before input parsed wrong")
    assert_equal(sample_1[0][1], [9, 2, 1, 2], "command input parsed wrong")
    assert_equal(sample_1[0][2], [3, 2, 2, 1], "after input parsed wrong")


def test_check_number_of_samples_with_3_or_more_matches_sample_input_1():
    number = p16.check_number_of_samples_with_3_or_more_matches(sample_input_1)
    assert_equal(number, 2)


def test_check_number_of_samples_with_3_or_more_matches_real():
    with open(input_file_path) as f:
        my_input = f.read()
    number = p16.check_number_of_samples_with_3_or_more_matches(my_input)
    assert_equal(number, 596)


def test_calculate_operations_real():
    with open(input_file_path) as f:
        my_input = f.read()
    number = p16.calculate_operations(my_input)
    assert_equal(number, 554)
