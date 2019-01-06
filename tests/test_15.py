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
sample_2 = """#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""
sample_3 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""
sample_4 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""
sample_5 = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""
sample_6 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""
sample_7 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""
sample_1_ordered = [Gnome(2, 1), Elf(4, 1), Elf(1, 2), Gnome(3, 2), Elf(5, 2), Gnome(2, 3), Elf(4, 3)]
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "15_input.txt")


def test_parse_input_sample_1():
    dungeon, creatures, num_e, num_g = p15.parse_input(sample_1)

    # Verify number of elves and gnomes
    assert_equal(num_e, 4, "Wrong number of elves")
    assert_equal(num_g, 3, "Wrong number of gnomes")
    # Verify dungeon
    tmp = sample_1.strip().split("\n")
    assert_equal(len(dungeon), len(tmp), f"Wrong number of rows in dungeon")
    for idx, row in enumerate(dungeon):
        assert_equal(row, tmp[idx], f"Wrong dungeon row on row idx {idx}")

    # Verify correct Creatures and order
    assert_equal(len(creatures), len(sample_1_ordered), f"Wrong number of creatures parsed")
    for idx, creature in enumerate(creatures):
        assert_equal(creature, sample_1_ordered[idx], f"wrong creature at idx {idx}")


def test_part_1_sample_2():
    ans = p15.part_1(sample_2)
    assert_equal(ans, 27730, "Wrong resulting answer")


def test_part_1_sample_3():
    ans = p15.part_1(sample_3)
    assert_equal(ans, 36334, "Wrong resulting answer")


def test_part_1_sample_4():
    ans = p15.part_1(sample_4)
    assert_equal(ans, 39514, "Wrong resulting answer")


def test_part_1_sample_5():
    ans = p15.part_1(sample_5)
    assert_equal(ans, 27755, "Wrong resulting answer")


def test_part_1_sample_6():
    ans = p15.part_1(sample_6)
    assert_equal(ans, 28944, "Wrong resulting answer")


def test_part_1_sample_7():
    ans = p15.part_1(sample_7)
    assert_equal(ans, 18740, "Wrong resulting answer")


def test_part_1_real():
    with open(input_file_path) as f:
        real_input = f.read()
    ans = p15.part_1(real_input)
    assert_equal(ans, 243390, "Wrong resulting answer")
