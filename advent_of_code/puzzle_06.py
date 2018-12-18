import numpy as np
import operator

def parse_input(my_in):
    pos_dict = dict()
    for i, pos in enumerate(my_in):
        x, y = pos.split(',')
        pos_dict[i] = int(x.strip()), int(y.strip())
    return pos_dict


def calc_manhattan_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def create_matrix(max_x, max_y):
    dt = np.dtype(('i4', 2))
    mat = np.empty((max_x, max_y), dtype=dt)
    mat.fill(-1)
    return mat


def get_req_mat_size(pos_dict):
    max_x = 0
    max_y = 0
    for p in pos_dict.values():
        if p[0] > max_x:
            max_x = p[0]
        if p[1] > max_y:
            max_y = p[1]
    return max_x + 1, max_y + 1


def fill_member(mat, id, pos, max_idx):
    #mat[pos] = [id, 0]

    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            dist = calc_manhattan_dist(pos, (x, y))
            if mat[x,y][0] == -1:
                mat[x,y] = [id, dist]
            elif dist < mat[x,y][1]:
                mat[x,y] = [id, dist]
            elif dist == mat[x,y][1]:
                mat[x,y] = [-2, dist]


def build_matrix(pos_dict):
    mat_size = get_req_mat_size(pos_dict)
    mat = create_matrix(mat_size[0], mat_size[1])
    for idx, pos in pos_dict.items():
        fill_member(mat, idx, pos, mat_size)
    return mat


def get_disqualified(mat):
    disq = set()
    x_len = mat.shape[0]
    y_len = mat.shape[1]
    for x in range(x_len):
        disq.add(mat[x,0][0])
        disq.add(mat[x, y_len - 1][0])
    for y in range(y_len):
        disq.add(mat[0, y][0])
        disq.add(mat[x_len - 1, y][0])
    return disq


def get_largest_patch(mat):
    disq = get_disqualified(mat)

    sizes = dict()
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            id = mat[x,y][0]
            if id in disq:
                continue
            elif id in sizes:
                sizes[id] += 1
            else:
                sizes[id] = 1
    sorted_sizes = sorted(sizes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_sizes[0]


def print_matrix(mat):
    for i in range(mat.shape[1]):
        row = list()
        for j in range(mat.shape[0]):
            row.append(mat[j,i][0])
        print(row)


def part_2(my_in, max_distance):
    pos_dict = parse_input(my_in)
    mat_size = get_req_mat_size(pos_dict)

    region_size = 0
    for x in range(mat_size[0]):
        for y in range(mat_size[1]):
            curr_dist = 0
            for pos in pos_dict.values():
                curr_dist += calc_manhattan_dist((x, y), pos)
                if curr_dist >= max_distance:
                    break
            if curr_dist < max_distance:
                region_size += 1

    return region_size


def part_1(my_in):
    mat = build_matrix(parse_input(my_in))
    return get_largest_patch(mat)
