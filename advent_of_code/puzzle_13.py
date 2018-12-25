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
    tunnel_system_dirty = my_input.split("\n")
    carts = []
    tunnel_system = []
    for y, line_dirty in enumerate(tunnel_system_dirty):
        line = find_and_add_carts_with_dir(line_dirty, left, y, carts)
        line = find_and_add_carts_with_dir(line, right, y, carts)
        line = find_and_add_carts_with_dir(line, upp, y, carts)
        line = find_and_add_carts_with_dir(line, down, y, carts)
        tunnel_system.append(line)
    return carts, tunnel_system


def move_cart(cart, tunnel_sys):
    cart.move_forward()
    curr_coord = cart.get_coordinates()
    current_tracktype = tunnel_sys[curr_coord[1]][curr_coord[0]]
    if current_tracktype == "-" or current_tracktype == "|":
        pass
    elif current_tracktype == "+":
        cart.intersect_rotate()
    else:
        cart.turn_rotate(current_tracktype)


def find_crash_in_sorted_carts(carts):
    prev_cart = None
    for cart in carts:
        if cart.is_crashed():
            continue
        if prev_cart is None:
            prev_cart = cart
            continue
        if cart.get_coordinates() == prev_cart.get_coordinates():
            cart.cart_crash(prev_cart)
            return cart.get_coordinates()
        else:
            prev_cart = cart
    return -1, -1


def find_first_crash(my_input):
    carts, tunnel_system = parse_input(my_input)
    carts.sort()
    while True:
        for cart in carts:
            move_cart(cart, tunnel_system)
            carts_sorted = sorted(carts)
            crash_coordinates = find_crash_in_sorted_carts(carts_sorted)
            if crash_coordinates != (-1, -1):
                return crash_coordinates
        carts.sort()


def find_last_uncrashed_cart(my_input):
    carts, tunnel_system = parse_input(my_input)
    while len(carts) > 1:
        carts.sort()
        for cart in carts:
            move_cart(cart, tunnel_system)
            carts_sorted = sorted(carts)
            find_crash_in_sorted_carts(carts_sorted)
        carts_temp = carts.copy()
        carts.clear()
        for cart in carts_temp:
            if not cart.is_crashed():
                carts.append(cart)
    if len(carts) == 1:
        return carts[0]
    return None
