from advent_of_code.utils.Path import Path


def add_path(new_paths, path, x, y, dungeon, covered_coord):
    # Continue with path if available space, and has not been visited earlier
    if dungeon[y][x] == "." and (x, y) not in covered_coord:
        tmp = Path(path.get_route())
        tmp.add_to_route((x, y))
        new_paths.append(tmp)


class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "NA"
        self.HP = 200
        self.AP = 3

    def get_coord(self):
        return self.x, self.y

    def set_new_coord(self, new_coord):
        self.x = new_coord[0]
        self.y = new_coord[1]

    def attack(self, other):
        """Attack other unit, return true if unit was killed."""
        other.HP -= self.AP
        return other.HP <= 0

    def reposition(self, dungeon):
        paths = self.calc_paths(dungeon)
        # no valid path, stand still
        if paths is None:
            return self.get_coord()

        # sort with inverted x/y for reading order
        end_points_xy_inv = set()
        for path in paths:
            end_points_xy_inv.add((path.route[-1][1], path.route[-1][0]))
        end_points_xy_inv = sorted(end_points_xy_inv)
        # swap target back to normal x/y coordinates
        target = end_points_xy_inv[0][1], end_points_xy_inv[0][0]
        valid_paths = [path for path in paths if path.route[-1] == target]
        follow_path = sorted(valid_paths)[0]
        if len(follow_path.route) > 1:
            return follow_path.route[1]
        else:
            return follow_path.route[0]

    def calc_paths(self, dungeon, paths=None, covered_coord=None):
        if paths is None:
            paths = list()
            paths.append(Path([self.get_coord()]))
        if covered_coord is None:
            covered_coord = set()

        # next to any enemy
        if self.type == "E":
            looking_for = "G"
        else:
            looking_for = "E"
        enemy_found = False
        for path in paths:
            x, y = path.get_route()[-1]
            if dungeon[y][x+1] == looking_for:
                path.add_enemy_found((x+1, y))
                enemy_found = True
            if dungeon[y+1][x] == looking_for:
                path.add_enemy_found((x, y+1))
                enemy_found = True
            if dungeon[y][x-1] == looking_for:
                path.add_enemy_found((x-1, y))
                enemy_found = True
            if dungeon[y-1][x] == looking_for:
                path.add_enemy_found((x, y-1))
                enemy_found = True
        if enemy_found:
            return [path for path in paths if path.found_enemy()]

        # take step for all paths
        new_paths = list()
        paths = sorted(paths)
        for path in paths:
            route = path.get_route()
            x, y = route[-1]

            # take a step in each direction
            add_path(new_paths, path, x+1, y, dungeon, covered_coord)
            add_path(new_paths, path, x, y+1, dungeon, covered_coord)
            add_path(new_paths, path, x-1, y, dungeon, covered_coord)
            add_path(new_paths, path, x, y-1, dungeon, covered_coord)
            # add coordinates to new visited coordinates
            covered_coord.add((x + 1, y))
            covered_coord.add((x, y + 1))
            covered_coord.add((x - 1, y))
            covered_coord.add((x, y-1))
        if len(new_paths) > 0:
            return self.calc_paths(dungeon, paths=new_paths, covered_coord=covered_coord)
        else:
            return None

    def __gt__(self, other):
        return (self.y, self.x) > (other.y, other.x)

    def __ge__(self, other):
        return (self.y, self.x) >= (other.y, other.x)

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def __le__(self, other):
        return (self.y, self.x) <= (other.y, other.x)

    def __eq__(self, other):
        return (self.y, self.x, self.type) <= (other.y, other.x, other.type)
