OPEN = "."
TREE = "|"
LUMBERYARD = "#"


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")
    area = list()
    for y in range(len(lines)):
        area.append(list())
        for char in lines[y]:
            area[y].append(char)
    return area


def get_at_position(area, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return area[y][x]
    except IndexError:
        return None


def resolve_open(area, x, y):
    num_trees = 0
    for idx_y in range(y-1, y+2):
        for idx_x in range(x-1, x+2):
            if get_at_position(area, idx_x, idx_y) == TREE:
                num_trees += 1
            if num_trees >= 3:
                return TREE
    return OPEN


def resolve_tree(area, x, y):
    num_lumberyards = 0
    for idx_y in range(y - 1, y + 2):
        for idx_x in range(x - 1, x + 2):
            if get_at_position(area, idx_x, idx_y) == LUMBERYARD:
                num_lumberyards += 1
            if num_lumberyards >= 3:
                return LUMBERYARD
    return TREE


def resolve_lumberyard(area, x, y):
    num_lumberyards = 0
    for idx_y in range(y - 1, y + 2):
        for idx_x in range(x - 1, x + 2):
            if get_at_position(area, idx_x, idx_y) == LUMBERYARD:
                num_lumberyards += 1
    num_trees = 0
    for idx_y in range(y - 1, y + 2):
        for idx_x in range(x - 1, x + 2):
            if get_at_position(area, idx_x, idx_y) == TREE:
                num_trees += 1
    if num_lumberyards >= 2 and num_trees >= 1:
        return LUMBERYARD
    else:
        return OPEN


def step_one_minute(area):
    area_new = list()
    for y, line in enumerate(area):
        area_new.append(list())
        for x, acre in enumerate(line):
            if acre == OPEN:
                area_new[y].append(resolve_open(area, x, y))
            elif acre == TREE:
                area_new[y].append(resolve_tree(area, x, y))
            else: # Lumberyard
                area_new[y].append(resolve_lumberyard(area, x, y))
    return area_new


def count_after_10_min(raw_input):
    area = parse_input(raw_input)
    for i in range(10):
        area = step_one_minute(area)
    return count_acres(area)


def count_acres(area):
    num_open, num_trees, num_lumberyards = 0, 0, 0
    for line in area:
        for acre in line:
            if acre == OPEN:
                num_open += 1
            elif acre == TREE:
                num_trees += 1
            else:
                num_lumberyards += 1
    return num_lumberyards, num_open, num_trees


def part_1(raw_input):
    num_lumberyards, num_open, num_trees = count_after_10_min(raw_input)
    return num_trees * num_lumberyards


def area_changed(prev_area, new_area):
    for y in range(len(prev_area)):
        for x in range(len(prev_area[y])):
            if prev_area[y][x] != new_area[y][x]:
                return True
    return False


def part_2(raw_input):
    area = parse_input(raw_input)
    areas = list()
    areas.append(area)
    repetition_rate = -1
    for passed_minutes in range(1000000000):
        area = step_one_minute(area)
        areas.append(area)
        for j in range(passed_minutes):
            if not area_changed(areas[passed_minutes-j], areas[passed_minutes+1]):
                repetition_rate = j
                break
        if repetition_rate >= 0:
            break
    num_lumberyards, num_open, num_trees = count_acres(area)
    passed_minutes += 1
    repetition_rate += 1
    print(passed_minutes)
    print(repetition_rate)
    minutes_left = 1000000000 - passed_minutes
    num_lumberyards, num_open, num_trees = count_acres(areas[passed_minutes - (repetition_rate - (minutes_left % repetition_rate))])
    return num_trees * num_lumberyards
