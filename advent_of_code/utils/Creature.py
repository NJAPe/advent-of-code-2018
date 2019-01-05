from advent_of_code.utils.Path import Path


def add_path(new_paths, path, x, y, dungeon):
    if dungeon[y][x] == ".":
        tmp = Path(path.get_route())
        tmp.add_to_route((x, y))
        new_paths.append(tmp)


class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "NA"

    def get_coord(self):
        return self.x, self.y

    def move(self, dungeon):
        paths = self.calc_paths(dungeon, 0)
        # no valid path, stand still
        if paths is None:
            return self.get_coord()

        # sort with inverted x/y for reading order
        end_points_xy_inv = set()
        for path in paths:
            end_points_xy_inv.add((path.route[-1][1],path.route[-1][0]))
        end_points_xy_inv = sorted(end_points_xy_inv)
        # swap target back to normal x/y coordinates
        target = end_points_xy_inv[0][1], end_points_xy_inv[0][0]
        valid_paths = [path for path in paths if path.route[-1] == target]
        return sorted(valid_paths)[0].route[1]

    def calc_paths(self, dungeon, taken_steps, paths=None, max_steps=20):
        if taken_steps > max_steps:
            return None
        taken_steps += 1
        if paths is None:
            paths = list()
            paths.append(Path([self.get_coord()]))

        # next to any enemy
        if self.type == "ELF":
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
        for path in paths:
            route = path.get_route()
            x, y = route[-1]
            last_pos = None
            if len(route) > 1:
                last_pos = route[-2]

            # take a step in each direction
            if not last_pos or last_pos != (x+1, y):
                add_path(new_paths, path, x+1, y, dungeon)
            if not last_pos or last_pos != (x, y+1):
                add_path(new_paths, path, x, y+1, dungeon)
            if not last_pos or last_pos != (x-1, y):
                add_path(new_paths, path, x-1, y, dungeon)
            if not last_pos or last_pos != (x, y-1):
                add_path(new_paths, path, x, y-1, dungeon)
        return self.calc_paths(dungeon, taken_steps, paths=new_paths, max_steps=max_steps)

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
