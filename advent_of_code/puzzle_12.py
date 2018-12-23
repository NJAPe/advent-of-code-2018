import os


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
    start_idx = curr_pop.find("#")
    if start_idx < 5:
        missing = 5 - start_idx
        curr_pop = missing*"." + curr_pop
        curr_offset += missing
    elif start_idx > 5:
        remove = start_idx - 5
        curr_pop = curr_pop[remove:]
        curr_offset -= remove
    end_idx = curr_pop.rfind("#")
    num_dots = len(curr_pop) - end_idx - 1
    if num_dots < 5:
        add_dots = 5 - num_dots
        curr_pop += add_dots*"."
    elif num_dots > 5:
        remove = num_dots - 5
        curr_pop = curr_pop[:-remove]
    next_pop = ""
    for idx in range(len(curr_pop)-3):
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

# Code used to find how the number of plants increases each generation
#sums = list()
#input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "12_input.txt")
#with open(input_file_path) as f:
#    my_input = f.read().strip()
#curr_pop, spread_patt = parse_input(my_input)
#curr_offset = 0
#for i in range(200):
#    curr_pop, curr_offset = calc_next_gen(curr_pop, spread_patt, curr_offset)
#    sums.append(calc_sum(curr_pop,curr_offset))
#    if i > 0:
#        print(f"{i}: current sum: {sums[i]}\t\t diff: {sums[i]-#sums[i-1]}")
