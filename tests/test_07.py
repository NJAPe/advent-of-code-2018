import advent_of_code.puzzle_07 as p07
from nose.tools import assert_equal
import os

sample_input = ["Step C must be finished before step A can begin.",
                "Step C must be finished before step F can begin.",
                "Step A must be finished before step B can begin.",
                "Step A must be finished before step D can begin.",
                "Step B must be finished before step E can begin.",
                "Step D must be finished before step E can begin.",
                "Step F must be finished before step E can begin."]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "07_input.txt")


def test_part_1_sample_input():
    order = p07.part_1(sample_input)
    assert_equal(order, "CABDFE", f"Expected order to be 'CABDFE', but was '{order}'")


def test_part_1_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip().split("\n")
    order = p07.part_1(real_input)
    assert_equal(order,
                 "FHMEQGIRSXNWZBCLOTUADJPKVY",
                 f"Expected order to be 'FHMEQGIRSXNWZBCLOTUADJPKVY', but was '{order}'")


def test_part_2_sample_input():
    seconds = p07.part_2(sample_input, 2, 0)
    assert_equal(seconds, 15, f"Expected the assembly to take 15 seconds, but took {seconds}")


def test_part_2_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip().split("\n")
    seconds = p07.part_2(real_input, 5, 60)
    assert_equal(seconds, 917, f"Expected the assembly to take 917 seconds, but took {seconds}")
