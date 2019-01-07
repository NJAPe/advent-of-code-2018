from advent_of_code.utils.Creature import Creature


class Elf(Creature):
    def __init__(self, x, y, attack_power=3):
        Creature.__init__(self, x, y)
        self.type = "E"
        self.AP = attack_power
