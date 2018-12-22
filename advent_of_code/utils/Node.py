class Node:
    def __init__(self, key, actions=1):
        self.blocked_by = dict()
        self.blocks = dict()
        self.key = key
        self.can_be_done = True
        self.actions_left = actions

    def add_blocker(self, other_node, key):
        self.can_be_done = False
        self.blocked_by[key] = other_node
        other_node.blocks[self.key] = self

    def remove_blocker(self, key):
        del self.blocked_by[key]
        if len(self.blocked_by) <= 0:
            self.can_be_done = True

    def can_be_started(self):
        return self.can_be_done

    def done(self):
        return self.actions_left <= 0

    def perform(self):
        if not self.can_be_done:
            print("what are you doing, I'm not ready yet")
            exit(1)
        self.actions_left -= 1
        if self.actions_left <= 0:
            for n in self.blocks.values():
                n.remove_blocker(self.key)
