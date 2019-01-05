class Path:
    def __init__(self, route):
        self.route = route.copy()
        self.enemies = list()

    def add_to_route(self, coord):
        self.route.append(coord)

    def add_enemy_found(self, coord):
        self.enemies.append(coord)

    def found_enemy(self):
        return len(self.enemies) > 0

    def get_route(self):
        return self.route

    def __gt__(self, other):
        return (self.route[1][1], self.route[1][0]) > (other.route[1][1], other.route[1][0])

    def __ge__(self, other):
        return (self.route[1][1], self.route[1][0]) >= (other.route[1][1], other.route[1][0])

    def __lt__(self, other):
        return (self.route[1][1], self.route[1][0]) < (other.route[1][1], other.route[1][0])

    def __le__(self, other):
        return (self.route[1][1], self.route[1][0]) <= (other.route[1][1], other.route[1][0])
