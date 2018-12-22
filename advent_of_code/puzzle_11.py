import math
import numpy as np


def calc_power_level(x, y, serial_id):
    rack_id = x + 10
    power_level = (rack_id * y + serial_id) * rack_id
    power_level = math.floor(power_level / 100) % 10 - 5
    return power_level


def build_summed_area_table(size_x, size_y, serial_id):
    summed_area = np.zeros((size_x, size_y), np.long)
    for y in range(1, size_y):
        for x in range(1, size_x):
            pl = calc_power_level(x, y, serial_id)
            summed_area[x, y] = pl + summed_area[x, y-1] + summed_area[x-1, y] - summed_area[x-1, y-1]
    return summed_area


def find_largest_3_by_3_area(size_x, size_y, serial_id):
    summed_area = build_summed_area_table(size_x, size_y, serial_id)
    return find_largest_square_of_size(3, summed_area, size_x, size_y)


def find_largest_square_of_size(square_size, summed_area, size_x, size_y):
    max_power = -1, -1, float("-inf")
    offset = square_size
    for y in range(1, size_y - offset):
        for x in range(1, size_x - offset):
            i_a = summed_area[x, y]
            i_b = summed_area[x + offset, y]
            i_c = summed_area[x, y + offset]
            i_d = summed_area[x + offset, y + offset]
            power_level = i_d + i_a - i_b - i_c
            if power_level > max_power[2]:
                max_power = x + 1, y + 1, power_level
    return max_power


def find_largest_square(size_x, size_y, serial_id):
    max_power_size = -1, -1, -1, float("-inf")
    summed_area = build_summed_area_table(size_x, size_y, serial_id)
    for i in range(1, 300 + 1):
        power_level = find_largest_square_of_size(i, summed_area, size_x, size_y)
        if power_level[2] > max_power_size[3]:
            max_power_size = power_level[0], power_level[1], i, power_level[2]
    return max_power_size
