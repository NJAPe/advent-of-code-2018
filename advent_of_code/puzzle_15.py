from advent_of_code.utils.Elf import Elf
from advent_of_code.utils.Gnome import Gnome


def parse_input(raw_input):
    raw_input = raw_input.strip()
    dungeon = raw_input.split("\n")
    creatures = list()
    for idx, row in enumerate(dungeon):
        i = row.find("E")
        while i >= 0:
            creatures.append(Elf(i, idx))
            i = row.find("E", i+1)
        i = row.find("G")
        while i >= 0:
            creatures.append(Gnome(i, idx))
            i = row.find("G", i + 1)
    return dungeon, sorted(creatures)
