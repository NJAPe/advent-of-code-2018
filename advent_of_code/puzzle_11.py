import math
import numpy as np


def calc_power_level(x, y, serial_id):
    rack_id = x + 10
    power_level = (rack_id * y + serial_id) * rack_id
    power_level = math.floor(power_level / 100) % 10 - 5
    return power_level


def build_power_matrix(size_x, size_y, serial_id):
    power_matrix = np.zeros((size_x, size_y), np.int16)
    for x in range(size_x):
        for y in range(size_y):
            power_matrix[x, y] = calc_power_level(x + 1, y + 1, serial_id)
    return power_matrix


def find_largest_3_by_3_area(size_x, size_y, serial_id):
    power_matrix = build_power_matrix(size_x, size_y, serial_id)
    return find_largest_square_of_size(3, power_matrix, size_x, size_y)


def find_largest_square_of_size(square_size, power_matrix, size_x, size_y):
    max_power = -1, -1, float("-inf")
    for x in range(size_x - (square_size - 1)):
        for y in range(size_y - (square_size - 1)):
            power_level = 0
            for row in range(square_size):
                for column in range(square_size):
                    power_level += int(power_matrix[x+column, y+row])
            if power_level > max_power[2]:
                max_power = x + 1, y + 1, power_level
    return max_power


def find_largest_square(size_x, size_y, serial_id):
    max_power_size = -1, -1, -1, float("-inf")
    power_matrix = build_power_matrix(size_x, size_y, serial_id)
    for i in range(1, 300 + 1):
        power_level = find_largest_square_of_size(i, power_matrix, size_x, size_y)
        if power_level[2] > max_power_size[3]:
            max_power_size = power_level[0], power_level[1], i, power_level[2]
    return max_power_size
