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
    return x_offset, topografy


def print_topografy(topografy):
    str = ""
    for line in topografy:
        for char in line:
            str += char
        str += "\n"
    print(str)
