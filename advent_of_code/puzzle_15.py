from advent_of_code.utils.Elf import Elf
from advent_of_code.utils.Gnome import Gnome


def parse_input(raw_input, elf_ap=3):
    raw_input = raw_input.strip()
    dungeon = raw_input.split("\n")
    creatures = list()
    num_e = 0
    num_g = 0
    for idx, row in enumerate(dungeon):
        i = row.find("E")
        while i >= 0:
            creatures.append(Elf(i, idx, elf_ap))
            num_e += 1
            i = row.find("E", i+1)
        i = row.find("G")
        while i >= 0:
            creatures.append(Gnome(i, idx))
            num_g += 1
            i = row.find("G", i + 1)
    return dungeon, sorted(creatures), num_e, num_g


def set_dungeon_tile(coord, dungeon, new_tile):
    dungeon[coord[1]] = dungeon[coord[1]][0:coord[0]] + new_tile + dungeon[coord[1]][coord[0] + 1:]


def reposition_creature(dungeon, creature):
    new_position = creature.reposition(dungeon)
    if new_position != creature.get_coord():
        # Remove creature from current position in dungeon
        set_dungeon_tile(creature.get_coord(), dungeon, ".")
        # Place creature at new position
        creature.set_new_coord(new_position)
        set_dungeon_tile(creature.get_coord(), dungeon, creature.type)


def get_creature(coord, creatures):
    for creature in creatures:
        if coord == creature.get_coord():
            return creature
    return None


def attack_adjacent_enemy(dungeon, creature, creatures):
    creature_killed = "NA"
    if creature.type == "G":
        looking_for = "E"
    else:
        looking_for = "G"

    enemies = list()
    x, y = creature.get_coord()
    if dungeon[y][x+1] == looking_for:
        enemies.append(get_creature((x+1, y), creatures))
    if dungeon[y][x-1] == looking_for:
        enemies.append(get_creature((x-1, y), creatures))
    if dungeon[y+1][x] == looking_for:
        enemies.append(get_creature((x, y+1), creatures))
    if dungeon[y-1][x] == looking_for:
        enemies.append(get_creature((x, y-1), creatures))
    # sort in reading order
    enemies = sorted(enemies)
    target = None
    for enemy in enemies:
        if target is None:
            target = enemy
        elif enemy.HP < target.HP:
            target = enemy
    if target is not None:
        if creature.attack(target):
            # target killed remove from dungeon
            set_dungeon_tile(target.get_coord(), dungeon, ".")
            creature_killed = looking_for
    return creature_killed


def print_dungeon_state(dungeon, creatures, number_of_turns):
    print_out = f"After {number_of_turns} rounds:\n"
    for y, line in enumerate(dungeon):
        idx = 0
        print_out += line + "  "
        while line.find("E", idx) >= 0 or line.find("G", idx) >= 0:
            e_idx = line.find("E", idx)
            g_idx = line.find("G", idx)
            if e_idx >= 0 and (g_idx < 0 or e_idx < g_idx):
                creature = get_creature((e_idx, y), creatures)
                print_out += f"{creature.type}({creature.HP}), "
                idx = e_idx + 1
            else:
                creature = get_creature((g_idx, y), creatures)
                print_out += f"{creature.type}({creature.HP}), "
                idx = g_idx + 1
        print_out += "\n"
    # print(print_out)


def part_1(raw_input):
    dungeon, creatures, num_e, num_g = parse_input(raw_input)
    no_enemy_found = False
    number_of_turns = 0
    print_dungeon_state(dungeon, creatures, number_of_turns)
    while not no_enemy_found:
        number_of_turns += 1
        for creature in creatures:
            if creature.HP <= 0:
                continue
            if creature.type == "E" and num_g <= 0:
                no_enemy_found = True
                break
            if creature.type == "G" and num_e <= 0:
                no_enemy_found = True
                break
            reposition_creature(dungeon, creature)
            print_dungeon_state(dungeon, creatures, number_of_turns)
            killed_creature = attack_adjacent_enemy(dungeon, creature, creatures)
            if killed_creature == "E":
                num_e -= 1
            elif killed_creature == "G":
                num_g -= 1
            else:
                pass
        creatures = [creature for creature in creatures if creature.HP > 0]
        creatures = sorted(creatures)
        print_dungeon_state(dungeon, creatures, number_of_turns)
    number_of_turns -= 1
    remaining_health = 0
    for creature in creatures:
        remaining_health += creature.HP
    return number_of_turns * remaining_health


def part_2(raw_input):
    elf_ap = 3
    elf_killed = True
    while elf_killed:
        elf_killed = False
        elf_ap += 1
        dungeon, creatures, num_e, num_g = parse_input(raw_input, elf_ap)

        no_enemy_found = False
        number_of_turns = 0
        while not no_enemy_found and not elf_killed:
            number_of_turns += 1
            for creature in creatures:
                if creature.HP <= 0:
                    continue
                if creature.type == "E" and num_g <= 0:
                    no_enemy_found = True
                    break
                if creature.type == "G" and num_e <= 0:
                    no_enemy_found = True
                    break
                reposition_creature(dungeon, creature)
                print_dungeon_state(dungeon, creatures, number_of_turns)
                killed_creature = attack_adjacent_enemy(dungeon, creature, creatures)
                if killed_creature == "E":
                    num_e -= 1
                    elf_killed = True
                    break
                elif killed_creature == "G":
                    num_g -= 1
                else:
                    pass
            creatures = [creature for creature in creatures if creature.HP > 0]
            creatures = sorted(creatures)
    number_of_turns -= 1
    remaining_health = 0
    for creature in creatures:
        remaining_health += creature.HP
    return number_of_turns * remaining_health
