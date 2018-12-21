import advent_of_code.puzzle_08 as p08
from nose.tools import assert_equal
import os

sample_input_meta_data = "1 1 2 10 11 12 2 99"
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "08_input.txt")


def test_sum_metadata_sample():
    sum = p08.sum_metadata(sample_input_meta_data)
    assert_equal(sum, 138, f"expected sum to be 138, but was {sum}")


def test_sum_metadata():
    with open(input_file_path) as f:
        meta_data_inp = f.read().strip()
    sum = p08.sum_metadata(meta_data_inp)
    assert_equal(sum, 49659, f"expected sum to be 49659, but was {sum}")
