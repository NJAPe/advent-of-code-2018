from advent_of_code.utils.Node import Node


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

    return order


def part_2(my_in, workers, task_offset=60):
    abc = "abcdefghijklmnopqrstuvwxyz"
    nodes = dict()
    for s in my_in:
        blocker = s[5]
        blocks = s[36]
        if blocker not in nodes:
            nodes[blocker] = Node(blocker, abc.find(blocker.lower()) + task_offset + 1)
        if blocks not in nodes:
            nodes[blocks] = Node(blocks, abc.find(blocks.lower()) + task_offset + 1)
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

    return seconds
