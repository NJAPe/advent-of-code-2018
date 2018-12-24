class Cart:
    turn_list = ["<", "|", ">"]
    directions = {"left":"<", "right":">", "upp":"^", "down":"v"}

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.cross_count = 0

    def get_coordinates(self):
        return self.x, self.y

    def get_direction(self):
        return self.direction

    def intersect_rotate(self):
        if self.cross_count % 3 == 1:
            # No change
            pass
        elif self.direction == "<":
            if self.cross_count % 3 == 0:
                self.direction = "v"
            elif self.cross_count % 3 == 2:
                self.direction = "^"
        elif self.direction == "v":
            if self.cross_count % 3 == 0:
                self.direction = ">"
            elif self.cross_count % 3 == 2:
                self.direction = "<"
        elif self.direction == ">":
            if self.cross_count % 3 == 0:
                self.direction = "^"
            elif self.cross_count % 3 == 2:
                self.direction = "v"
        elif self.direction == "^":
            if self.cross_count % 3 == 0:
                self.direction = "<"
            elif self.cross_count % 3 == 2:
                self.direction = ">"
        self.cross_count += 1

    def move_forward(self):
        if self.direction == ">":
            self.x += 1
        elif self.direction == "<":
            self.x -= 1
        elif self.direction == "^":
            self.y -= 1
        elif self.direction == "v":
            self.y += 1

    def turn_rotate(self, turn):
        if turn == "/":
            if self.direction == ">":
                self.direction = "^"
            elif self.direction == "<":
                self.direction = "v"
            elif self.direction == "^":
                self.direction = ">"
            elif self.direction == "v":
                self.direction = "<"
        elif turn == "\\":
            if self.direction == ">":
                self.direction = "v"
            elif self.direction == "<":
                self.direction = "^"
            elif self.direction == "^":
                self.direction = "<"
            elif self.direction == "v":
                self.direction = ">"
