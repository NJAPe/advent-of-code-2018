import advent_of_code.puzzle_04 as p04
from nose.tools import assert_equal
import os

sample_input=["[1518-11-05 00:03] Guard #99 begins shift",
       "[1518-11-01 00:00] Guard #10 begins shift",
       "[1518-11-05 00:45] falls asleep",
       "[1518-11-01 00:30] falls asleep",
       "[1518-11-03 00:29] wakes up",
       "[1518-11-04 00:02] Guard #99 begins shift",
       "[1518-11-01 00:55] wakes up",
       "[1518-11-01 23:58] Guard #99 begins shift",
       "[1518-11-02 00:40] falls asleep",
       "[1518-11-02 00:50] wakes up",
       "[1518-11-03 00:05] Guard #10 begins shift",
       "[1518-11-03 00:24] falls asleep",
       "[1518-11-04 00:36] falls asleep",
       "[1518-11-04 00:46] wakes up",
       "[1518-11-01 00:05] falls asleep",
       "[1518-11-01 00:25] wakes up",
       "[1518-11-05 00:55] wakes up",
       ""]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "04_input.txt")


def test_part_1_sample_input():
    my_answer = p04.calc_strategy1(sample_input)
    assert_equal(my_answer, 240, f"expected answer to be 240 but was {my_answer}")


def test_part_1_real_input():
    with open(input_file_path) as f:
        real_input = f.read().split("\n")
    my_answer = p04.calc_strategy1(real_input)
    assert_equal(my_answer, 87681, f"expected answer to be 87681 but was {my_answer}")


def test_part_2_sample_input():
    my_answer = p04.calc_strategy2(sample_input)
    assert_equal(my_answer, 4455, f"expected answer to be 4455, but was {my_answer}")


def test_part_2_real_input():
    with open(input_file_path) as f:
        real_input = f.read().split("\n")
    my_answer = p04.calc_strategy2(real_input)
    assert_equal(my_answer, 136461, f"expected answer to be 136461, but was {my_answer}")
