import advent_of_code.puzzle_02 as p02
from nose.tools import assert_equal
import os


sample_inp = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
sample_inp2 = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "02_input.txt")


def test_checksum_sample_input():
    checksum = p02.calc_checksum(sample_inp)
    assert_equal(checksum, 12, f"Expected checksum to be 12, but was {checksum}")


def test_checksum_real_input():
    checksum = p02.calc_checksum(p02.get_codes_from_file(input_file_path))
    assert_equal(checksum, 7936, f"Expected checksum to ve 7936, but was {checksum}")


def test_similar_id_sample_input():
    similar_str = p02.solve_part2(sample_inp2)
    assert_equal(similar_str, "fgij", f"Expected similar string to be 'fgij', but was'{similar_str}'")


def test_similar_id_real_input():
    similar_str = p02.solve_part2(p02.get_codes_from_file(input_file_path))
    assert_equal(similar_str, "lnfqdscwjyteorambzuchrgpx", f"Expected similar string to be 'lnfqdscwjyteorambzuchrgpx', but was'{similar_str}'")
