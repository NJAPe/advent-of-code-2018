import advent_of_code.puzzle_12 as p12
from nose.tools import assert_equal, assert_true, assert_false
import os

sample_input = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "12_input.txt")


def test_get_spread_pattern_should_add():
    spread_input = ["..#.. => #"]
    spread_pattern = p12.get_spread_pattern(spread_input)
    assert_true("..#.." in spread_pattern, "expected input to have been added")


def test_get_spread_pattern_should_not_add():
    spread_input = ["..#.. => ."]
    spread_pattern = p12.get_spread_pattern(spread_input)
    assert_false("..#.." in spread_pattern, "expected input to not have been added")


def test_parse_input_sample():
    init_state, spread_patt = p12.parse_input(sample_input)
    assert_equal(init_state, "#..#.#..##......###...###", "wrong initial state parsed")
    assert_true("...##" in spread_patt, "should be in spread pattern")


def test_next_generation_sample():
    correct_next_gen = "#...#....#.....#..#..#..#"
    init_state, spread_patt = p12.parse_input(sample_input)
    next_gen, offset = p12.calc_next_gen(init_state, spread_patt, 0)
    assert_true(next_gen.find(correct_next_gen) != -1, f"could not find correct in {next_gen}")
    assert_equal(next_gen.count("#"), correct_next_gen.count("#"), "not correct number of plants")


def test_next_x3_generation_sample():
    correct_next_gen = "#.#...#..#.#....#..#..#...#"
    init_state, spread_patt = p12.parse_input(sample_input)
    next_gen, offset = p12.calc_next_gen(init_state, spread_patt, 0)
    next_gen, offset = p12.calc_next_gen(next_gen, spread_patt, offset)
    next_gen, offset = p12.calc_next_gen(next_gen, spread_patt, offset)
    assert_true(next_gen.find(correct_next_gen) != -1, f"could not find correct in {next_gen}")
    assert_equal(next_gen.count("#"), correct_next_gen.count("#"), "not correct number of plants")


def test_calc_to_gen_20_sample():
    correct_20_gen = "#....##....#####...#######....#.#..##"
    next_gen, offset = p12.calc_to_generations(sample_input, 20)
    assert_true(next_gen.find(correct_20_gen) != -1, f"could not find correct in {next_gen}")
    assert_equal(next_gen.count("#"), correct_20_gen.count("#"), "not correct number of plants")
    assert_equal(offset, 10, f"not correct offset calculated{next_gen}")


def test_calc_sum_sample():
    state, offset = p12.calc_to_generations(sample_input, 20)
    my_sum = p12.calc_sum(state, offset)
    assert_equal(my_sum, 325, "wrong sum calculated")


def test_calc_sum_real():
    with open(input_file_path) as f:
        my_input = f.read().strip()
    state, offset = p12.calc_to_generations(my_input, 20)
    my_sum = p12.calc_sum(state, offset)
    assert_equal(my_sum, 3890, "wrong sum calculated")
