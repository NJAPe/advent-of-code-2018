from advent_of_code.utils.Cart import Cart

left = "<"
right = ">"
upp = "^"
down = "v"


def find_and_add_carts_with_dir(line, direction, y_pos, carts):
    x_pos = line.find(direction)
    while x_pos > 0:
        carts.append(Cart(x_pos, y_pos, direction))

        # replace cart symbol with track
        if direction == "<" or direction == ">":
            repl_str = "-"
        else:
            repl_str = "|"
        line = line[:x_pos] + repl_str + line[x_pos+1:]

        # next cart
        x_pos = line.find(direction)
    return line


def parse_input(my_input):
    tunnel_system_dirty = my_input.strip().split("\n")
    carts = []
    tunnel_system = []
    for y, line_dirty in enumerate(tunnel_system_dirty):
        line = find_and_add_carts_with_dir(line_dirty, left, y, carts)
        line = find_and_add_carts_with_dir(line, right, y, carts)
        line = find_and_add_carts_with_dir(line, upp, y, carts)
        line = find_and_add_carts_with_dir(line, down, y, carts)
        tunnel_system.append(line)
    return carts, tunnel_system
