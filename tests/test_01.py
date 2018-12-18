import advent_of_code.puzzle_01 as p01
import os
from nose.tools import assert_equal

sample_inp = ["+1", "-2", "+3", "+1"]
input_file_path = os.path.join(os.path.dirname(__file__), '..', 'inputs', '01_input.txt')


def test_sample_input_part1():
    freq = p01.add_freq_shift(sample_inp)
    assert_equal(freq, 3, f'expected frequency to be 3, but was {freq}')


def test_sample_input_part1_with_pos_offset():
    freq = p01.add_freq_shift(sample_inp, 3)
    assert_equal(freq, 6, f'expected frequency to be 6, but was {freq}')


def test_sample_input_part1_with_neg_offset():
    freq = p01.add_freq_shift(sample_inp, -3)
    assert_equal(freq, 0, f'expected frequency to be 0, but was {freq}')


def test_real_input_part1():
    with open(input_file_path) as f:
        real_input = f.read().split("\n")
    freq = p01.add_freq_shift(real_input)
    assert_equal(freq, 442, f'expected frequency to be 442, but was {freq}')


def test_sample_input_part2():
    freq = p01.find_first_duplicate_freq2(sample_inp)
    assert_equal(freq, 2, f'expected first repetitive frequency to be 2, but was {freq}')


def test_sample_input_part2_with_pos_offset():
    freq = p01.find_first_duplicate_freq2(sample_inp, 2)
    assert_equal(freq, 4, f'expected first repetitive frequency to be 4, but was {freq}')


def test_sample_input_part2_with_neg_offset():
    freq = p01.find_first_duplicate_freq2(sample_inp, -2)
    assert_equal(freq, 0, f'expected first repetitive frequency to be 0, but was {freq}')


def test_real_input_part2():
    with open(input_file_path) as f:
        real_input = f.read().split("\n")
    freq = p01.find_first_duplicate_freq2(real_input)
    assert_equal(freq, 59908, f'expected first repetitive frequency to be 0, but was {freq}')
