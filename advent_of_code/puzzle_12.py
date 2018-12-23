def get_spread_pattern(spread_input):
    spread_pattern = set()
    for line in spread_input:
        if line == "":
            continue
        if line[0] == "." or line[0] == "#":
            pattern = line[0:5]
            result = line[-1]
            if result == "#":
                spread_pattern.add(pattern)
    return spread_pattern


def parse_input(my_input):
    input_array = my_input.strip().split("\n")
    start_idx = min(input_array[0].find("."), input_array[0].find("#"))
    init_state = input_array[0][start_idx:]
    spread_pattern = get_spread_pattern(input_array)
    return init_state, spread_pattern


def calc_next_gen(curr_pop, spread_pattern, curr_offset):
    if curr_pop[0:5] != ".....":
        curr_pop = "....." + curr_pop
        curr_offset += 5
    if curr_pop[-5:] != ".....":
        curr_pop += "....."
    next_pop = ""
    for idx in range(len(curr_pop)-1):
        key = curr_pop[idx-2:idx+3]
        if key in spread_pattern:
            next_pop += "#"
        else:
            next_pop += "."
    return next_pop, curr_offset


def calc_to_generations(my_input, target_gen):
    curr_pop, spread_patt = parse_input(my_input)
    curr_offset = 0
    for i in range(target_gen):
        curr_pop, curr_offset = calc_next_gen(curr_pop, spread_patt, curr_offset)
    return curr_pop, curr_offset


def calc_sum(state, offset):
    my_sum = 0
    for idx, c in enumerate(state):
        if c == "#":
            my_sum += idx - offset
    return my_sum
