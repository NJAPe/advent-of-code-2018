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


def part_1(my_in):
    nodes = dict()
    for s in my_in:
        blocker = s[5]
        blocks = s[36]
        if blocker not in nodes:
            nodes[blocker] = Node(blocker)
        if blocks not in nodes:
            nodes[blocks] = Node(blocks)
        nodes[blocks].add_blocker(nodes[blocker], blocker)

    order = ""
    while len(nodes) > 0:
        ready = set()
        for k, v in nodes.items():
            if v.can_be_started():
                ready.add(k)
        next = sorted(ready)[0]
        print(f"next is {next}")
        nodes[next].perform()
        del nodes[next]
        order += next

    print(f"The correct mounting order is '{order}'")


def part_2(my_in, workers):
    abc = "abcdefghijklmnopqrstuvwxyz"
    nodes = dict()
    for s in my_in:
        blocker = s[5]
        blocks = s[36]
        if blocker not in nodes:
            nodes[blocker] = Node(blocker, abc.find(blocker.lower()) + 61)
        if blocks not in nodes:
            nodes[blocks] = Node(blocks, abc.find(blocks.lower()) + 61)
        nodes[blocks].add_blocker(nodes[blocker], blocker)

    in_progress = dict()
    seconds = 0
    while len(nodes) > 0:
        seconds += 1
        ready = set()
        for k, v in nodes.items():
            if v.can_be_started():
                ready.add(k)
        waiting = sorted(ready)
        for node in waiting:
            if len(in_progress) >= workers:
                break
            elif node not in in_progress:
                in_progress[node] = nodes[node]
        done = set()
        for key, node in in_progress.items():
            node.perform()
            if node.done():
                done.add(key)

        for d in done:
            del in_progress[d]
            del nodes[d]

    print(f"It took '{seconds}' seconds")


my_in = ["Step C must be finished before step A can begin.",
"Step C must be finished before step F can begin.",
"Step A must be finished before step B can begin.",
"Step A must be finished before step D can begin.",
"Step B must be finished before step E can begin.",
"Step D must be finished before step E can begin.",
"Step F must be finished before step E can begin."]

with open("07_input.txt") as f:
    my_in = f.read().strip().split("\n")
part_1(my_in)
part_2(my_in, 5)
