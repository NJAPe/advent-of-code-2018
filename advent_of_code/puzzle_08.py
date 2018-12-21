class Tree:
    def __init__(self):
        self.children = list()
        self.metadata = list()

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, meta):
        self.metadata.append(meta)

    def get_children(self):
        return self.children

    def get_metadata(self):
        return self.metadata


def build_tree(tree_def_inp):
    tree_def = tree_def_inp.strip().split(" ")
    tree_def = [int(t) for t in tree_def]
    idx, tree_head = parse_tree(tree_def, 0)
    return tree_head


def parse_tree(tree_def, idx):
    num_childs = tree_def[idx]
    idx += 1
    num_metadata = tree_def[idx]
    idx += 1
    tree = Tree()
    for i in range(num_childs):
        idx, child = parse_tree(tree_def, idx)
        tree.add_child(child)
    for i in range(idx, idx + num_metadata):
        tree.add_metadata(tree_def[i])
    idx += num_metadata
    return idx, tree


def sum_metadata(tree_head):
    sum = 0
    for c in tree_head.get_children():
        sum += sum_metadata(c)
    for meta in tree_head.get_metadata():
        sum += meta
    return sum
