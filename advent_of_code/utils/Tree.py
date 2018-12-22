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
