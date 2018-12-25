import advent_of_code.puzzle_14 as p14
from nose.tools import assert_equal
import os


def test_after_9():
    answer = p14.get_ten_after_x(9)
    assert_equal(answer, "5158916779", "Wrong answer")


def test_after_5():
    answer = p14.get_ten_after_x(5)
    assert_equal(answer, "0124515891", "Wrong answer")


def test_after_18():
    answer = p14.get_ten_after_x(18)
    assert_equal(answer, "9251071085", "Wrong answer")


def test_after_2018():
    answer = p14.get_ten_after_x(2018)
    assert_equal(answer, "5941429882", "Wrong answer")


def test_after_540561():
    answer = p14.get_ten_after_x(540561)
    assert_equal(answer, "1413131339", "Wrong answer")


def test_recipes_to_51589():
    num_recipes = p14.get_find_number_of_recipes_to_get_x("51589")
    assert_equal(num_recipes, 9, "wrong number of recipes")


def test_recipes_to_01245():
    num_recipes = p14.get_find_number_of_recipes_to_get_x("01245")
    assert_equal(num_recipes, 5, "wrong number of recipes")


def test_recipes_to_92510():
    num_recipes = p14.get_find_number_of_recipes_to_get_x("92510")
    assert_equal(num_recipes, 18, "wrong number of recipes")


def test_recipes_to_59414():
    num_recipes = p14.get_find_number_of_recipes_to_get_x("59414")
    assert_equal(num_recipes, 2018, "wrong number of recipes")


def test_recipes_to_540561():
    num_recipes = p14.get_find_number_of_recipes_to_get_x("540561")
    assert_equal(num_recipes, 20254833, "wrong number of recipes")
