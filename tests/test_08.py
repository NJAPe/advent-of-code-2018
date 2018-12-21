import advent_of_code.puzzle_08 as p08
from nose.tools import assert_equal
import os

sample_input_meta_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "08_input.txt")


def test_sum_metadata_sample():
    tree_head = p08.build_tree(sample_input_meta_data)
    meta_sum = p08.sum_metadata(tree_head)
    assert_equal(meta_sum, 138, f"expected meta_sum to be 138, but was {meta_sum}")


def test_sum_metadata():
    with open(input_file_path) as f:
        meta_data_inp = f.read().strip()
    tree_head = p08.build_tree(meta_data_inp)
    meta_sum = p08.sum_metadata(tree_head)
    assert_equal(meta_sum, 36891, f"expected meta_sum to be 36891, but was {meta_sum}")
