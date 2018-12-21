import advent_of_code.puzzle_09 as p09
from nose.tools import assert_equal
import os

input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "09_input.txt")


def test_9_players_25_max():
    max_score = p09.play_game(9, 25)
    assert_equal(max_score, 32, f"expected max_score to be 32, but was {max_score}")


def test_10_players_1618_max():
    max_score = p09.play_game(10, 1618)
    assert_equal(max_score, 8317, f"expected max_score to be 8317, but was {max_score}")


def test_13_players_7999_max():
    max_score = p09.play_game(13, 7999)
    assert_equal(max_score, 146373, f"expected max_score to be 146373, but was {max_score}")


def test_17_players_1104_max():
    max_score = p09.play_game(17, 1104)
    assert_equal(max_score, 2764, f"expected max_score to be 2764, but was {max_score}")


def test_21_players_6111_max():
    max_score = p09.play_game(21, 6111)
    assert_equal(max_score, 54718, f"expected max_score to be 54718, but was {max_score}")


def test_30_players_5807_max():
    max_score = p09.play_game(30, 5807)
    assert_equal(max_score, 37305, f"expected max_score to be 37305, but was {max_score}")


def test_455_players_71223_max():
    max_score = p09.play_game(455, 71223)
    assert_equal(max_score, 384288, f"expected max_score to be 384288, but was {max_score}")


def test_455_players_7122300_max():
    max_score = p09.play_game(455, 7122300)
    assert_equal(max_score, 3189426841, f"expected max_score to be 3189426841, but was {max_score}")
