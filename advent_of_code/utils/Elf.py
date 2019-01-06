from advent_of_code.utils.Creature import Creature


class Elf(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, x, y)
        self.type = "E"
