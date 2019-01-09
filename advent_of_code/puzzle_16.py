from advent_of_code.utils.Operations import *


a_and_b_as_registers = [addr, mulr, banr, borr, setr, gtrr, eqrr]
only_a_as_register = [addi, muli, bani, bori, gtri, eqri]
only_b_as_register = [gtir, eqir]
none_as_register = [seti]
all_operators = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtrr, gtri, gtir, eqrr, eqri, eqir]


def parse_sample_inputs(raw_input):
    raw_input = raw_input.strip()
    input_list = raw_input.split("\n")
    samples = list()
    line_idx = 0
    while line_idx < len(input_list) and \
            (input_list[line_idx].find("Before") >= 0 or input_list[line_idx].strip() == ""):
        line = input_list[line_idx]
        if line == "":
            line_idx += 1
            continue
        before = line[line.find("[")+1:line.find("]")].split(",")
        before = list(map(int, before))
        line_idx += 1

        command = input_list[line_idx].strip().split(" ")
        command = list(map(int, command))
        line_idx += 1

        line = input_list[line_idx]
        after = line[line.find("[")+1:line.find("]")].split(",")
        after = list(map(int, after))
        line_idx += 1
        samples.append((before, command, after))
    return samples, line_idx


def parse_operations(raw_input, line_idx):
    raw_input = raw_input.strip()
    input_list = raw_input.split("\n")
    commands = list()
    for idx in range(line_idx, len(input_list)):
        command = input_list[idx].strip().split(" ")
        command = list(map(int, command))
        commands.append(command)
    return commands


def value_can_be_index(idx):
    return 0 <= idx <= 3


def compare_result_from_operator(opfunction, a, b, expected_ans, registers):
    try:
        return expected_ans == opfunction(a, b, registers)
    except IndexError:
        return False


def check_sample_against_operators_3_or_more_matches(a, b, expected_ans, registers):
    num_matches = 0
    if value_can_be_index(a) and value_can_be_index(b):
        for opfunc in a_and_b_as_registers:
            if compare_result_from_operator(opfunc, a, b, expected_ans, registers):
                num_matches += 1
                if num_matches >= 3:
                    return True
    if value_can_be_index(a):
        for opfunc in only_a_as_register:
            if compare_result_from_operator(opfunc, a, b, expected_ans, registers):
                num_matches += 1
                if num_matches >= 3:
                    return True
    if value_can_be_index(b):
        for opfunc in only_b_as_register:
            if compare_result_from_operator(opfunc, a, b, expected_ans, registers):
                num_matches += 1
                if num_matches >= 3:
                    return True
    for opfunc in none_as_register:
        if compare_result_from_operator(opfunc, a, b, expected_ans, registers):
            num_matches += 1
            if num_matches >= 3:
                return True
    return num_matches >= 3


def check_number_of_samples_with_3_or_more_matches(raw_input):
    samples, line_idx = parse_sample_inputs(raw_input)
    number_of_samples_with_3_or_more = 0
    for before, command, after in samples:
        expected_ans = after[command[3]]
        if check_sample_against_operators_3_or_more_matches(command[1], command[2], expected_ans, before):
            number_of_samples_with_3_or_more += 1
    return number_of_samples_with_3_or_more


def remove_all_non_matching(before, command, after, possible_opcodes):
    op_to_remove = list()
    for operator in possible_opcodes:
        try:
            if compare_result_from_operator(operator, command[1], command[2], after[command[3]], before):
                pass
            else:
                op_to_remove.append(operator)
        except Exception:
            op_to_remove.append(operator)
    for operator in op_to_remove:
        possible_opcodes.remove(operator)


def remove_operator_from_all_other_lists(operator, opcode, opcode_map):
    for i in range(16):
        if i == opcode:
            continue
        if operator in opcode_map[i]:
            opcode_map[i].remove(operator)


def find_opcodes(samples):
    opcode_map = dict()
    for i in range(16):
        opcode_map[i] = all_operators.copy()

    for before, command, after in samples:
        oplist = opcode_map[command[0]]
        if len(oplist) == 1:
            continue # opcode have already been resolved
        remove_all_non_matching(before, command, after, oplist)
        if len(oplist) == 1:
            remove_operator_from_all_other_lists(oplist[0], command[0], opcode_map)

    for i in range(16):
        for operator in all_operators:
            opcodes = list()
            for opcode, oplist in opcode_map.items():
                if operator in oplist:
                    opcodes.append(opcode)
            if len(opcodes) == 1:
                opcode_map[opcodes[0]] = [operator]
                remove_operator_from_all_other_lists(operator, opcodes[0], opcode_map)

    for i in range(16):
        if len(opcode_map[i]) != 1:
            raise Exception
        else:
            opcode_map[i] = opcode_map[i][0]
    return opcode_map


def calculate_operations(raw_input):
    samples, line_idx = parse_sample_inputs(raw_input)
    opcode_map = find_opcodes(samples)
    commands = parse_operations(raw_input, line_idx)
    register = samples[-1][2]
    for command in commands:
        register[command[3]] = opcode_map[command[0]](command[1], command[2], register)
    return register[0]
