import numpy as np
import os


class Point:
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.x_speed = speed_x
        self.y_speed = speed_y

    def step_forward(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def step_back(self):
        self.x -= self.x_speed
        self.y -= self.y_speed

    def get_coordinates(self):
        return self.x, self.y


def parse_input(input_points):
    my_points = list()

    coordinate_string = "position=<"
    velocity_string = "velocity=<"
    for line in input_points:
        start_pos = line.find(coordinate_string) + len(coordinate_string)
        end_pos = line.find(">", start_pos)
        coordinates = line[start_pos:end_pos].split(",")

        start_pos = line.find(velocity_string) + len(velocity_string)
        end_pos = line.find(">", start_pos)
        velocities = line[start_pos:end_pos].split(",")

        my_points.append(Point(int(coordinates[0].strip()),
                               int(coordinates[1].strip()),
                               int(velocities[0].strip()),
                               int(velocities[1].strip())))
    return my_points


def print_image(data, size_x, size_y):
    image_str = ""
    for y in range(size_y):
        for x in range(size_x):
            if data[x, y] == 0:
                image_str += "."
            else:
                image_str += "#"
        image_str += "\n"
    return image_str


def update_min_max(my_points):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for idx, point in enumerate(my_points):
        x, y = point.get_coordinates()
        if idx == 0:
            min_x, max_x = x, x
            min_y, max_y = y, y
        else:
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y
    return min_x, min_y, max_x, max_y


def get_sizes(min_x, min_y, max_x, max_y):
    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    return size_x, size_y


def step_and_print_image(my_points):
    # Initialize min/max/size
    min_x, min_y, max_x, max_y = update_min_max(my_points)
    size_x, size_y = get_sizes(min_x, min_y, max_x, max_y)

    # Step forward until area starts increasing
    min_area = size_x * size_y
    counter = 0
    while size_x * size_y <= min_area:
        counter += 1
        for point in my_points:
            point.step_forward()

        min_x, min_y, max_x, max_y = update_min_max(my_points)
        size_x, size_y = get_sizes(min_x, min_y, max_x, max_y)
        if size_x * size_y < min_area:
            min_area = size_x * size_y

    # Take one step back
    counter -= 1
    for point in my_points:
        point.step_back()
    min_x, min_y, max_x, max_y = update_min_max(my_points)
    size_x, size_y = get_sizes(min_x, min_y, max_x, max_y)

    # Create light matrix
    data = np.zeros((size_x, size_y), np.uint8)
    for point in my_points:
        x, y = point.get_coordinates()
        data[x - min_x, y - min_y] = 1

    # Create image string
    img_str = print_image(data, size_x, size_y)
    print(img_str)
    return counter, img_str
