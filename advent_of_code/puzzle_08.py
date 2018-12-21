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


def sum_tree_metadata(tree_head):
    meta_sum = 0
    for c in tree_head.get_children():
        meta_sum += sum_tree_metadata(c)
    meta_sum += sum(tree_head.get_metadata())
    return meta_sum


def calculate_node_sum(node):
    number_of_children = len(node.get_children())
    if number_of_children<= 0:
        return sum(node.get_metadata())
    
    meta_sum = 0
    for meta in node.get_metadata():
        if meta > number_of_children:
            continue
        meta_sum += calculate_node_sum(node.get_children()[meta-1])
    return meta_sum
