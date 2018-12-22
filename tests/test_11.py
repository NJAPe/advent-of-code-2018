import advent_of_code.puzzle_11 as p11
from nose.tools import assert_equal


def test_calc_power_level_sample_1():
    power_level = p11.calc_power_level(3, 5, 8)
    assert_equal(power_level, 4, "Wrong power level")


def test_calc_power_level_sample_2():
    power_level = p11.calc_power_level(122, 79, 57)
    assert_equal(power_level, -5, "Wrong power level")


def test_calc_power_level_sample_3():
    power_level = p11.calc_power_level(217, 196, 39)
    assert_equal(power_level, 0, "Wrong power level")


def test_calc_power_level_sample_4():
    power_level = p11.calc_power_level(101, 153, 71)
    assert_equal(power_level, 4, "Wrong power level")


def test_find_largest_3_by_3_sample_1():
    max_power = p11.find_largest_3_by_3_area(301, 301, 18)
    assert_equal(max_power[0], 33, f"{max_power}Wrong x-position of top-left corner")
    assert_equal(max_power[1], 45, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 29, "Wrong max-power value")


def test_find_largest_3_by_3_sample_2():
    max_power = p11.find_largest_3_by_3_area(301, 301, 42)
    assert_equal(max_power[0], 21, "Wrong x-position of top-left corner")
    assert_equal(max_power[1], 61, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 30, "Wrong max-power value")


def test_find_largest_3_by_3_real():
    max_power = p11.find_largest_3_by_3_area(301, 301, 8444)
    assert_equal(max_power[0], 243, "Wrong x-position of top-left corner")
    assert_equal(max_power[1], 68, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 28, "Wrong max-power value")


def test_find_largest_any_sample_1():
    max_power = p11.find_largest_square(300, 300, 18)
    assert_equal(max_power[0], 90, "Wrong x-position of top-left corner")
    assert_equal(max_power[1], 269, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 16, "Wrong square size")
    assert_equal(max_power[3], 113, "Wrong max-power value")


def test_find_largest_any_sample_2():
    max_power = p11.find_largest_square(300, 300, 42)
    assert_equal(max_power[0], 232, "Wrong x-position of top-left corner")
    assert_equal(max_power[1], 251, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 12, "Wrong square size")
    assert_equal(max_power[3], 119, "Wrong max-power value")


def test_find_largest_any_real():
    max_power = p11.find_largest_square(300, 300, 8444)
    assert_equal(max_power[0], 236, "Wrong x-position of top-left corner")
    assert_equal(max_power[1], 252, "Wrong y-position of top-left corner")
    assert_equal(max_power[2], 12, "Wrong square size")
    assert_equal(max_power[3], 96, "Wrong max-power value")

