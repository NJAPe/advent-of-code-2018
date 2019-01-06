from nose.tools import assert_equal
from advent_of_code.utils.Elf import Elf
from advent_of_code.utils.Gnome import Gnome

dungeon = ["#######", "#.E...#", "#.....#", "#...G.#", "#######"]
dungeon_no_gnome = ["#######", "#.E...#", "#.....#", "#.....#", "#######"]
dungeon_adjacent = ["#######", "#.EG..#", "#.....#", "#.....#", "#######"]


def test_attack_once():
    my_gnome = Gnome(1, 1)
    my_elf = Elf(1, 2)
    my_elf.attack(my_gnome)
    assert_equal(my_elf.HP, 200, "The attacker shall not have lost any health")
    assert_equal(my_gnome.HP, 197, "The attacked unit shall have lost 3 HP")

def test_attack_until_dead():
    my_gnome = Gnome(1, 1)
    my_elf = Elf(1, 2)
    attacks = 1
    while not my_gnome.attack(my_elf):
        attacks += 1
    assert_equal(my_gnome.HP, 200, "The attacker shall not have lost any health")
    assert_equal(my_elf.HP, -1, "Elf shall have -1 health left when dead")
    assert_equal(attacks, 67, "It should have taken 67 attacks to kill the elf")

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
    next_coord = my_elf.reposition(dungeon)
    assert_equal(next_coord, (3, 1), "wrong new position")


def test_move_no_gnome():
    my_elf = Elf(2, 1)
    next_coord = my_elf.reposition(dungeon_no_gnome)
    assert_equal(next_coord, (2, 1), "wrong new position")


def test_move_adjacent_creatures():
    my_elf = Elf(2, 1)
    next_coord = my_elf.reposition(dungeon_adjacent)
    assert_equal(next_coord, (2, 1), "wrong new position")
