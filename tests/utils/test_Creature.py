from nose.tools import assert_equal
from advent_of_code.utils.Elf import Elf

dungeon = ["#######", "#.E...#", "#.....#", "#...G.#", "#######"]
dungeon_no_gnome = ["#######", "#.E...#", "#.....#", "#.....#", "#######"]


def test_calc_paths():
    my_elf = Elf(2, 1)
    paths = my_elf.calc_paths(dungeon)
    assert_equal(len(paths), 6, "Expected 6 valid paths")
    assert_equal(len(paths[0].route), 4, "Should be four coordinates in path")


def test_calc_paths_no_gnome():
    my_elf = Elf(2, 1)
    paths = my_elf.calc_paths(dungeon_no_gnome)
    assert_equal(paths, None, "expected there to be no valid path")


def test_move():
    my_elf = Elf(2, 1)
    next_coord = my_elf.move(dungeon)
    assert_equal(next_coord, (3, 1), "wrong new position")


def test_move_no_gnome():
    my_elf = Elf(2, 1)
    next_coord = my_elf.move(dungeon_no_gnome)
    assert_equal(next_coord, (2, 1), "wrong new position")
