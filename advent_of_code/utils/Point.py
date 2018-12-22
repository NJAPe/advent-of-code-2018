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
