import advent_of_code.puzzle_15 as p15
from nose.tools import assert_equal, assert_true, assert_false
from advent_of_code.utils.Gnome import Gnome
from advent_of_code.utils.Elf import Elf
import os

sample_1 = """#######
#.G.E.#
#E.G.E#
#.G.E.#
#######
"""
sample_1_ordered = [Gnome(2, 1), Elf(4, 1), Elf(1, 2), Gnome(3, 2), Elf(5, 2), Gnome(2, 3), Elf(4, 3)]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "15_input.txt")


def test_parse_input_sample_1():
    dungeon, creatures = p15.parse_input(sample_1)

    # Verify dungeon
    tmp = sample_1.strip().split("\n")
    assert_equal(len(dungeon), len(tmp), f"Wrong number of rows in dungeon")
    for idx, row in enumerate(dungeon):
        assert_equal(row, tmp[idx], f"Wrong dungeon row on row idx {idx}")

    # Verify correct Creatures and order
    assert_equal(len(creatures), len(sample_1_ordered), f"Wrong number of creatures parsed")
    for idx, creature in enumerate(creatures):
        assert_equal(creature, sample_1_ordered[idx], f"wrong creature at idx {idx}")
