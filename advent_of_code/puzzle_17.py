def get_min_max(line, key):
    idx = line.find(key) + 2
    part = line[idx:line.find(" ", idx)].strip()
    if part[-1] == ",":
        part = part[:-1]
    if part.find("..") != -1:
        part = line[idx:].strip()
        min_part, max_part = part.split("..")
        return int(min_part), int(max_part)
    else:
        return int(part), int(part)


def update_min_max(line, curr_max, curr_min, key):
    temp_min, temp_max = get_min_max(line, key)
    if temp_max > curr_max:
        curr_max = temp_max
    if temp_min < curr_min:
        curr_min = temp_min
    return curr_min, curr_max


def parse_input(raw_input):
    input_list = raw_input.strip().split("\n")
    min_x = 500
    min_y = float("inf")
    max_x = 500
    max_y = float("-inf")
    for line in input_list:
        min_x, max_x = update_min_max(line, max_x, min_x, "x=")
        min_y, max_y = update_min_max(line, max_y, min_y, "y=")
    x_offset = min_x - 1

    # Create only sand
    topografy = list()
    for y in range(max_y + 1):
        topografy.append(list())
        for x in range(x_offset, max_x + 2):
            topografy[y].append(".")

    # Add clay
    for line in input_list:
        x_1, x_2 = get_min_max(line, "x=")
        y_1, y_2 = get_min_max(line, "y=")
        for y in range(y_1, y_2 + 1):
            for x in range(x_1 - x_offset, x_2 - x_offset + 1):
                topografy[y][x] = "#"
    # Add well
    topografy[0][500-x_offset] = "+"
    return x_offset, min_y, max_y, topografy


def print_topografy(topografy):
    str = ""
    for line in topografy:
        for char in line:
            str += char
        str += "\n"
    print(str)


DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3
RET_HIT_WALL = 4
RET_FULL = 5
RET_DONE = 6
def fill_water(x, y, direction, fill_type, topo):
    if direction == DOWN:
        y += 1
    elif direction == UP:
        y -= 1
    elif direction == LEFT:
        x -= 1
    elif direction == RIGHT:
        x += 1
    else:
        pass # Unknown direction

    if y >= len(topo):
        return RET_DONE
    if topo[y][x] == "#":
        return RET_HIT_WALL
    elif topo[y][x] == "~":
        return RET_FULL
    topo[y][x] = fill_type
    if y + 1 >= len(topo):
        return fill_water(x, y, DOWN, "|", topo)
    if topo[y+1][x] == "#" or topo[y+1][x] == "~":
        # non-penetrable surface
        if direction != DOWN:
            return fill_water(x, y, direction, fill_type, topo)
        else:
            # spread in right and left direction
            ret_right = fill_water(x, y, RIGHT, fill_type, topo)
            ret_left = fill_water(x, y, LEFT, fill_type, topo)
            if (ret_right == RET_HIT_WALL or ret_right == RET_FULL) and (ret_left == RET_HIT_WALL or ret_left == RET_FULL):
                topo[y][x] = "~"
                fill_water(x, y, RIGHT, "~", topo)
                fill_water(x, y, LEFT, "~", topo)
                return RET_FULL
    else:
        # Penetrable surface
        ret = fill_water(x, y, DOWN, "|", topo)
        if ret == RET_FULL:
            # spread in right and left direction
            ret_right = fill_water(x, y, RIGHT, "|", topo)
            ret_left = fill_water(x, y, LEFT, "|", topo)
            if ret_right == RET_HIT_WALL and ret_left == RET_HIT_WALL:
                topo[y][x] = "~"
                fill_water(x, y, RIGHT, "~", topo)
                fill_water(x, y, LEFT, "~", topo)
                return RET_FULL
            elif ret_right == RET_FULL or ret_left == RET_FULL:
                return RET_FULL


def analyze_well(raw_input):
    x_offset, min_y, max_y, topo = parse_input(raw_input)
    fill_water(500 - x_offset, 0, DOWN, "|", topo)
    still = 0
    flowing = 0
    for y in range(min_y, max_y+1):
        line = topo[y]
        for char in line:
            if char == "|":
                flowing += 1
            elif char == "~":
                still += 1
    return still, flowing
